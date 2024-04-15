import sys
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

dataset = load_dataset("openai_humaneval")

def evaluate_model(model_name):
    
    # Load model and tokenizer from Hugging Face
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Iterate over the tasks in the dataset
    for i, task in enumerate(dataset['test']):
        # Prepare the prompt
        prompt = task['prompt']
        
        # Generate the completion using the model
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=256, num_return_sequences=1)
        completion = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Save the generated code to a file
        file_name = f"generated_solution_{i+1}.py"
        with open(file_name, 'w') as file:
            file.write("# Generated code for task " + str(i+1) + "\n")
            file.write("def solution():\n")
            # Ensuring the generated code is correctly indented as a function body
            completion_indented = '\n'.join('    ' + line for line in completion.split('\n'))
            file.write(completion_indented)
            file.write("\n\n# You can add tests or other function calls here.\n")

    return "Completed writing generated code to files."