import subprocess
import re

def _construct_program(model_output_prefix: str,
                       function_code: str,
                       generated_test: str) -> str:
    with open("/tmp/{model_output_prefix}_test.py", "w") as file:
        file.write('import unittest\n')
        file.write('from unittest import TestCase\n')
        file.write(function_code)
        file.write('\n')
        file.write(generated_test)
        file.write('\n')
    return "/tmp/{model_output_prefix}_test.py"


def execute(model_output_prefix: str,
            function_code: str,
            generated_test: str):
    program_name = _construct_program(
        model_output_prefix, function_code, generated_test)
    r = subprocess.run(
        f"cat {program_name} evaluate_base.py > evaluate.py",
        shell=True, text=True)
    result = subprocess.run(["python", "evaluate.py"],
                            capture_output=True, text=True)

    formatted_output = f"Return Code: {result.returncode}\n \
        --- STDOUT ---\n{result.stdout}\n \
        --- STDERR ---\n{result.stderr}"
    
    print(result.stderr)
    # Check if there were failures
    pattern = r"failures=\d+"
    match = re.search(pattern, formatted_output)

    return match == None, formatted_output
