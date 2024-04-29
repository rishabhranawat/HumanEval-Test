import os
import sys

import inflect
import openai
import time
from datasets import load_dataset

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

openai.api_key = OPEN_AI_API_KEY
client = openai.OpenAI()

inflect_engine = inflect.engine()
dataset = load_dataset("THUDM/humaneval-x")

def get_model_completion(model, function_code, task_id_class):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an expert test software engineer."
            },
            {
                "role": "user",
                "content": f"For the following Python function, \
                    create a unnittest class named {task_id_class} that tests this function appropriately. \
                        Do not include the actual input function \n \
                        Do not include any import statements. \n \
                        Do not output anything other than the {task_id_class} class definition itself.\
                        Do not include any comments. \n \
                        ```{function_code}```"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

def evaluate_model(model_name, model_output_prefix):
    generated_test_classes = []
    for i, task in enumerate(dataset['test']):
        if i % 10 == 0:
            time.sleep(10)
            print('Sleeping for 10s to avoid getting rate limited.')
        try:
            print(f"Running HumanEval-Test generation for {i+1}")

            declaration = task['declaration']
            canonical_solution = task['canonical_solution']
            function_code = declaration + '\n' + canonical_solution
            
            # get task_id in alphabetical form.
            task_id = inflect_engine.number_to_words(int(task['task_id'].split('/')[1]))
            test_class_name = f'{task_id.capitalize()}Test'

            # generate the actual completion using the specified model
            completion = get_model_completion(model_name, function_code, test_class_name)

            completion_indented = '\n'.join(line for line in completion.split('\n'))
            completion_indented = completion_indented.replace('```python', '')\
                .replace('```', '')\
                    .replace("if __name__ == \'__main__\':", "")\
                        .replace("unittest.main()", "")

            generated_test_classes.append(completion_indented)
        except Exception as e:
            print(f"There was an exception, stopping at task {i}", e)
            break

    with open(f"{model_output_prefix}_test.py", 'w') as file:
        file.write('\n'.join(generated_test_classes))

    return "Completed writing generated code to files."

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <model_name> <model_output_prefix>")
        sys.exit(1)
    
    model_name = sys.argv[1]
    model_output_prefix =sys.argv[2]
    
    print(f"Running Inference for Model: {model_name} and for output_prefix: {model_output_prefix}")
    evaluate_model(model_name, model_output_prefix)