from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
        for idx, elem in enumerate(numbers):
            for idx2, elem2 in enumerate(numbers):
                if idx != idx2:
                    distance = abs(elem - elem2)
                    if distance < threshold:
                        return True
    
        return False
    

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
        result = []
        current_string = []
        current_depth = 0
    
        for c in paren_string:
            if c == '(':
                current_depth += 1
                current_string.append(c)
            elif c == ')':
                current_depth -= 1
                current_string.append(c)
    
                if current_depth == 0:
                    result.append(''.join(current_string))
                    current_string.clear()
    
        return result
    

def truncate_number(number: float) -> float:
        return number % 1.0
    

from typing import List


def below_zero(operations: List[int]) -> bool:
        balance = 0
    
        for op in operations:
            balance += op
            if balance < 0:
                return True
    
        return False
    

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
        mean = sum(numbers) / len(numbers)
        return sum(abs(x - mean) for x in numbers) / len(numbers)
    