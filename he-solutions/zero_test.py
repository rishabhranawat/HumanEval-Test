import unittest
import coverage

from zero import has_close_elements

class Test(unittest.TestCase):

    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 1.0), False)
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.0), False)
    
if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    t = Test()
    t.test_has_close_elements()

    cov.stop()
    cov.save()
    print(cov.report())

    # To get coverage data as numbers
    # Get the analysis for the specific module
    print(cov.analysis('zero.py'))
    _, covered, missing, _ = cov.analysis('zero.py')

    # # Calculate the coverage percentage
    total_lines = len(covered) + len(missing)
    coverage_percent = (len(covered) / total_lines) * 100 if total_lines > 0 else 100

    print(f"Coverage for module.py: {coverage_percent:.2f}%")
