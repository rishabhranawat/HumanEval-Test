import unittest
import coverage
import inflect

import numpy as np

from solutions import *

engine = inflect.engine()

def compute_coverage(test_module):
    try:
        loader = unittest.TestLoader()

        # Load tests from the class
        suite = loader.loadTestsFromTestCase(test_module)

        # Create a test runner and run the tests
        runner = unittest.TextTestRunner()
        runner.run(suite)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    scores = []
    
    cov = coverage.Coverage(source=['solutions'])
    cov.start()
    
    for i in range(0, 5):
        task_id = engine.number_to_words(i)
        test_class_name = f'{task_id.capitalize()}Test'
        compute_coverage(globals().get(test_class_name))
    
    cov.stop()
    cov.save()

    print(cov.report())