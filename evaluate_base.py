import unittest
import coverage
import inflect

import numpy as np

from solutions import *

engine = inflect.engine()

def compute_coverage(test_module):
    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()

    # Load tests from the class
    suite = loader.loadTestsFromTestCase(test_module)

    # Create a test runner and run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
    cov.stop()
    cov.save()

    _, covered, missing, _ = cov.analysis("evaluate.py")

    total_lines = len(covered) + len(missing)
    coverage_percent = (len(covered) / total_lines) * 100 if total_lines > 0 else 100
    return coverage_percent

if __name__ == "__main__":
    scores = []
    for i in range(0, 1):
        task_id = engine.number_to_words(i)
        test_class_name = f'{task_id.capitalize()}Test'
        print(f"Computing Coverage for test {test_class_name}")
        scores.append(compute_coverage(globals().get(test_class_name)))

    print(f"Average coverage: {np.mean(scores):.2f}%")
    print(f"Minimum coverage: {np.min(scores):.2f}%")
    print(f"Maximum coverage: {np.max(scores):.2f}%")
    print(f"Standard deviation: {np.std(scores):.2f}%")
    print(f"Median coverage: {np.median(scores):.2f}%")