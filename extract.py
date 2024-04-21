'''
Extracts the solutions from the HumanEval-X dataset and writes them to a solutions.py
file.

'''
import inflect

from datasets import load_dataset

inflect_engine = inflect.engine()
dataset = load_dataset("THUDM/humaneval-x")

def _extract_solutions():

    all_solutions = []
    for i, task in enumerate(dataset['test']):
        print(f"Running HumanEval-Test Code Extraction for {i+1}")

        declaration = task['declaration']
        canonical_solution = task['canonical_solution']
        
        indented_solution = '\n'.join('    ' + line for line in canonical_solution.split('\n'))
        complete_solution = declaration + indented_solution
        all_solutions.append(complete_solution)

    with open("solutions.py", "w") as file:
        file.write("\n\n".join(all_solutions))
    return "Completed writing generated code to files."

if __name__ == '__main__':
    _extract_solutions()