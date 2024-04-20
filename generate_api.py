import sys
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from openai import OpenAI
import os

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

dataset = load_dataset("openai_humaneval")
client = OpenAI(
  api_key=TOGETHER_API_KEY,
  base_url='https://api.together.xyz/v1',
)

def get_model_completion(model, prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "system",
            "content": "You are an experiment software engineer.",
            },
            {
            "role": "user",
            "content": f"Write a comprehensive test suite in Python for the following scenario \n {prompt}",
            }
        ],
        model=model
    )
    return chat_completion.choices[0].message.content

def evaluate_model(model_name, model_output_prefix):
    # Iterate over the tasks in the dataset
    for i, task in enumerate(dataset['test']):
        print(f"Running HumanEval-Test generation for {i+1}")
        # Prepare the prompt
        prompt = task['prompt']
        canonical_solution = task['canonical_solution']
        input_prompt = f"{prompt} \n We can solve this using the following Python program: \n {canonical_solution}"
        
        completion = get_model_completion(model_name, input_prompt)

        # Save the generated code to a file
        file_name = f"{model_output_prefix}/{task['task_id'].split('/')[1]}.py"
        with open(file_name, 'w') as file:
            file.write("# Generated code for task " + str(i+1) + "\n")
            file.write("def solution():\n")
            # Ensuring the generated code is correctly indented as a function body
            completion_indented = '\n'.join('    ' + line for line in completion.split('\n'))
            file.write(completion_indented)
            file.write("\n\n# You can add tests or other function calls here.\n")

    return "Completed writing generated code to files."

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <model_name> <model_output_prefix>")
        sys.exit(1)
    model_name = sys.argv[1]
    model_output_prefix =sys.argv[2]
    print(f"Running Inference for Model: {model_name} and for output_prefix: {model_output_prefix}")
    evaluate_model(model_name, model_output_prefix)