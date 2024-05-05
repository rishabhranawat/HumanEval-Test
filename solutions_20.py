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
    

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
        if not numbers:
            return []
    
        result = []
    
        for n in numbers[:-1]:
            result.append(n)
            result.append(delimeter)
    
        result.append(numbers[-1])
    
        return result
    

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
        def parse_paren_group(s):
            depth = 0
            max_depth = 0
            for c in s:
                if c == '(':
                    depth += 1
                    max_depth = max(depth, max_depth)
                else:
                    depth -= 1
    
            return max_depth
    
        return [parse_paren_group(x) for x in paren_string.split(' ') if x]
    

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
        return [x for x in strings if substring in x]
    

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
        sum_value = 0
        prod_value = 1
    
        for n in numbers:
            sum_value += n
            prod_value *= n
        return sum_value, prod_value
    

from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
        running_max = None
        result = []
    
        for n in numbers:
            if running_max is None:
                running_max = n
            else:
                running_max = max(running_max, n)
    
            result.append(running_max)
    
        return result
    

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
        if not string:
            return ''
    
        beginning_of_suffix = 0
    
        while not is_palindrome(string[beginning_of_suffix:]):
            beginning_of_suffix += 1
    
        return string + string[:beginning_of_suffix][::-1]
    

from typing import List


def string_xor(a: str, b: str) -> str:
        def xor(i, j):
            if i == j:
                return '0'
            else:
                return '1'
    
        return ''.join(xor(x, y) for x, y in zip(a, b))
    

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
        if not strings:
            return None
    
        maxlen = max(len(x) for x in strings)
        for s in strings:
            if len(s) == maxlen:
                return s
    

def greatest_common_divisor(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    

from typing import List


def all_prefixes(string: str) -> List[str]:
        result = []
    
        for i in range(len(string)):
            result.append(string[:i+1])
        return result
    

def string_sequence(n: int) -> str:
        return ' '.join([str(x) for x in range(n + 1)])
    

def count_distinct_characters(string: str) -> int:
        return len(set(string.lower()))
    

from typing import List


def parse_music(music_string: str) -> List[int]:
        note_map = {'o': 4, 'o|': 2, '.|': 1}
        return [note_map[x] for x in music_string.split(' ') if x]
    

def how_many_times(string: str, substring: str) -> int:
        times = 0
    
        for i in range(len(string) - len(substring) + 1):
            if string[i:i+len(substring)] == substring:
                times += 1
    
        return times
    

from typing import List


def sort_numbers(numbers: str) -> str:
        value_map = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }
        return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))


