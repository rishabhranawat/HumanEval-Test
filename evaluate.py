import os
import sys
import subprocess

def run_tests(generated_tests_dir, model_name):
    # Get all test files in the specified directory
    test_files = [f for f in os.listdir(generated_tests_dir) if f.endswith('.py')]
    test_results = []

    # Loop through each test file
    for test_file in test_files:
        # Construct the path to the test file
        test_path = os.path.join(generated_tests_dir, test_file)
        
        # Run the test file as a separate Python process
        result = subprocess.run([sys.executable, test_path, model_name], capture_output=True, text=True)
        
        # Check the result
        if result.returncode == 0:
            test_results.append((test_file, 'Pass'))
        else:
            test_results.append((test_file, 'Fail', result.stdout, result.stderr))

    # Output the results of the tests
    for test_file, status, stdout, stderr in test_results:
        print(f"Test File: {test_file} - Status: {status}")
        if status == 'Fail':
            print(f"Stdout: {stdout}")
            print(f"Stderr: {stderr}")

if __name__ == "__main__":
    generated_tests_dir = sys.argv[1]
    model_name = sys.argv[2]
    run_tests(generated_tests_dir, model_name)
