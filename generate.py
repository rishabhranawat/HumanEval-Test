import sys
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from openai import OpenAI
import os
import inflect

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

inflect_engine = inflect.engine()
dataset = load_dataset("THUDM/humaneval-x")
client = OpenAI(
  api_key=TOGETHER_API_KEY,
  base_url='https://api.together.xyz/v1',
)

def get_model_completion(model, prompt, task_id):
    chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "system",
            "content": "You are an expert software engineer. \
                You make sure that your code is runnable as is and you do not write unnecesary comments.",
            },
            {
            "role": "user",
            "content": f"Write a comprehensive test suite in Python for the following function: \n {prompt}. \n \
                Please do not include any explanation or the actual function itself. 
                Create the output such that it is a Python file itself. \
                ",
            }
        ],
        model=model
    )
    return chat_completion.choices[0].message.content

def evaluate_model(model_name, model_output_prefix):
    # Iterate over the tasks in the dataset
    for i, task in enumerate(dataset['test']):
        if i > 4: break
        print(f"Running HumanEval-Test generation for {i+1}")
        canonical_solution = task['canonical_solution']
        
        task_id = inflect_engine.number_to_words(int(task['task_id'].split('/')[1]))

        completion = get_model_completion(model_name, canonical_solution, task_id)

        # Save the generated code to a file
        file_name = f"{model_output_prefix}/{task_id}.py"
        with open(file_name, 'w') as file:
            # Ensuring the generated code is correctly indented as a function body
            completion_indented = '\n'.join('    ' + line for line in completion.split('\n'))
            file.write(completion_indented)

    return "Completed writing generated code to files."

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <model_name> <model_output_prefix>")
        sys.exit(1)
    model_name = sys.argv[1]
    model_output_prefix =sys.argv[2]
    print(f"Running Inference for Model: {model_name} and for output_prefix: {model_output_prefix}")
    evaluate_model(model_name, model_output_prefix)