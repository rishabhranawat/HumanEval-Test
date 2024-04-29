'''
Extracts the solutions from the HumanEval-X dataset and writes them to a solutions.py
file.

'''

from datasets import load_dataset


def _extract_solutions():
    """
    Extracts solutions from the HumanEval-X dataset.

    This function loads the HumanEval-X dataset from the Hugging Face datasets library,
    iterates over the test set, and appends each solution to the all_solutions list.

    Prints the progress of extraction for each test case.

    Returns:
        all_solutions (list): A list of all solutions from the test set of the HumanEval-X dataset.
    """
    dataset = load_dataset("THUDM/humaneval-x")

    all_solutions = []
    for i, task in enumerate(dataset['test']):
        print(f"Running HumanEval-Test Code Extraction for {i+1}")

        declaration = task['declaration']
        canonical_solution = task['canonical_solution']

        indented_solution = '\n'.join(
            '    ' + line for line in canonical_solution.split('\n'))
        complete_solution = declaration + indented_solution
        all_solutions.append(complete_solution)

    with open("solutions.py", "w") as file:
        file.write("\n\n".join(all_solutions))
    return "Completed writing generated code to files."


if __name__ == '__main__':
    _extract_solutions()
