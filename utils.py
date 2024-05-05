def format_generated_output(completion: str) -> str:
    completion_indented = '\n'.join(
        line for line in completion.split('\n'))
    completion_indented = completion_indented.replace('```python', '')\
        .replace('```', '')\
        .replace("if __name__ == \'__main__\':", "")\
        .replace("if __name__ == \"__main__\":", "")\
        .replace("unittest.main()", "")\
        .replace("import unittest", "")
    return completion_indented