import unittest

import coverage

from solutions import *


def compute_coverage():
    try:
        loader = unittest.TestLoader()

        # Load tests from the class
        suite = loader.discover('.', pattern='evaluate.py')

        # Create a test runner and run the tests
        runner = unittest.TextTestRunner()
        runner.run(suite)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    scores = []

    cov = coverage.Coverage(source=['solutions'])
    cov.start()
    compute_coverage()
    cov.stop()
    cov.save()

    print(cov.report())
