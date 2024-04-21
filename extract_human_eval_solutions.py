import inflect

from datasets import load_dataset

inflect_engine = inflect.engine()
dataset = load_dataset("THUDM/humaneval-x")

def _extract_solutions():

    for i, task in enumerate(dataset['test']):
        if i > 4: break
        print(f"Running HumanEval-Test Code Extraction for {i+1}")

        declaration = task['declaration']
        canonical_solution = task['canonical_solution']
        
        # Save the generated code to a file
        task_id = inflect_engine.number_to_words(int(task['task_id'].split('/')[1]))
        file_name = f"he-solutions/{task_id}.py"
        with open(file_name, 'w') as file:
            file.write(declaration + "\n")

            # Ensuring the generated code is correctly indented as a function body
            completion_indented = '\n'.join('    ' + line for line in canonical_solution.split('\n'))
            file.write(completion_indented)
            file.write("\n\n# You can add tests or other function calls here.\n")

    return "Completed writing generated code to files."

if __name__ == '__main__':
    _extract_solutions()