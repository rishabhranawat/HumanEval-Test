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
    

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
        closest_pair = None
        distance = None
    
        for idx, elem in enumerate(numbers):
            for idx2, elem2 in enumerate(numbers):
                if idx != idx2:
                    if distance is None:
                        distance = abs(elem - elem2)
                        closest_pair = tuple(sorted([elem, elem2]))
                    else:
                        new_distance = abs(elem - elem2)
                        if new_distance < distance:
                            distance = new_distance
                            closest_pair = tuple(sorted([elem, elem2]))
    
        return closest_pair
    

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
        min_number = min(numbers)
        max_number = max(numbers)
        return [(x - min_number) / (max_number - min_number) for x in numbers]
    

from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
        return [x for x in values if isinstance(x, int)]
    

def strlen(string: str) -> int:
        return len(string)
    

def largest_divisor(n: int) -> int:
        for i in reversed(range(n)):
            if n % i == 0:
                return i
    

from typing import List


def factorize(n: int) -> List[int]:
        import math
        fact = []
        i = 2
        while i <= int(math.sqrt(n) + 1):
            if n % i == 0:
                fact.append(i)
                n //= i
            else:
                i += 1
    
        if n > 1:
            fact.append(n)
        return fact
    

from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
        import collections
        c = collections.Counter(numbers)
        return [n for n in numbers if c[n] <= 1]
    

def flip_case(string: str) -> str:
        return string.swapcase()
    

from typing import List


def concatenate(strings: List[str]) -> str:
        return ''.join(strings)
    

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
        return [x for x in strings if x.startswith(prefix)]
    

def get_positive(l: list):
        return [e for e in l if e > 0]
    

def is_prime(n):
        if n < 2:
            return False
        for k in range(2, n - 1):
            if n % k == 0:
                return False
        return True
    

import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
        begin, end = -1., 1.
        while poly(xs, begin) * poly(xs, end) > 0:
            begin *= 2.0
            end *= 2.0
        while end - begin > 1e-10:
            center = (begin + end) / 2.0
            if poly(xs, center) * poly(xs, begin) > 0:
                begin = center
            else:
                end = center
        return begin
    

def sort_third(l: list):
        l = list(l)
        l[::3] = sorted(l[::3])
        return l
    

def unique(l: list):
        return sorted(list(set(l)))
    

def max_element(l: list):
        m = l[0]
        for e in l:
            if e > m:
                m = e
        return m
    

def fizz_buzz(n: int):
        ns = []
        for i in range(n):
            if i % 11 == 0 or i % 13 == 0:
                ns.append(i)
        s = ''.join(list(map(str, ns)))
        ans = 0
        for c in s:
            ans += (c == '7')
        return ans
    

def sort_even(l: list):
        evens = l[::2]
        odds = l[1::2]
        evens.sort()
        ans = []
        for e, o in zip(evens, odds):
            ans.extend([e, o])
        if len(evens) > len(odds):
            ans.append(evens[-1])
        return ans
    

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
        return encode_cyclic(encode_cyclic(s))
    

def prime_fib(n: int):
        import math
    
        def is_prime(p):
            if p < 2:
                return False
            for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
                if p % k == 0:
                    return False
            return True
        f = [0, 1]
        while True:
            f.append(f[-1] + f[-2])
            if is_prime(f[-1]):
                n -= 1
            if n == 0:
                return f[-1]
    

def triples_sum_to_zero(l: list):
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                for k in range(j + 1, len(l)):
                    if l[i] + l[j] + l[k] == 0:
                        return True
        return False
    

def car_race_collision(n: int):
        return n**2
    

def incr_list(l: list):
        return [(e + 1) for e in l]
    

def pairs_sum_to_zero(l):
        for i, l1 in enumerate(l):
            for j in range(i + 1, len(l)):
                if l1 + l[j] == 0:
                    return True
        return False
    

def change_base(x: int, base: int):
        ret = ""
        while x > 0:
            ret = str(x % base) + ret
            x //= base
        return ret
    

def triangle_area(a, h):
        return a * h / 2.0
    

def fib4(n: int):
        results = [0, 0, 2, 0]
        if n < 4:
            return results[n]
    
        for _ in range(4, n + 1):
            results.append(results[-1] + results[-2] + results[-3] + results[-4])
            results.pop(0)
    
        return results[-1]
    

def median(l: list):
        l = sorted(l)
        if len(l) % 2 == 1:
            return l[len(l) // 2]
        else:
            return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0
    

def is_palindrome(text: str):
        for i in range(len(text)):
            if text[i] != text[len(text) - 1 - i]:
                return False
        return True
    

def modp(n: int, p: int):
        ret = 1
        for i in range(n):
            ret = (2 * ret) % p
        return ret
    

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
        return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
    

def remove_vowels(text):
        return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])
    

def below_threshold(l: list, t: int):
        for e in l:
            if e >= t:
                return False
        return True
    

def add(x: int, y: int):
        return x + y
    

def same_chars(s0: str, s1: str):
        return set(s0) == set(s1)
    

def fib(n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)
    

def correct_bracketing(brackets: str):
        depth = 0
        for b in brackets:
            if b == "<":
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                return False
        return depth == 0
    

def monotonic(l: list):
        if l == sorted(l) or l == sorted(l, reverse=True):
            return True
        return False
    

def common(l1: list, l2: list):
        ret = set()
        for e1 in l1:
            for e2 in l2:
                if e1 == e2:
                    ret.add(e1)
        return sorted(list(ret))
    

def largest_prime_factor(n: int):
        def is_prime(k):
            if k < 2:
                return False
            for i in range(2, k - 1):
                if k % i == 0:
                    return False
            return True
        largest = 1
        for j in range(2, n + 1):
            if n % j == 0 and is_prime(j):
                largest = max(largest, j)
        return largest
    

def sum_to_n(n: int):
        return sum(range(n + 1))
    

def correct_bracketing(brackets: str):
        depth = 0
        for b in brackets:
            if b == "(":
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                return False
        return depth == 0
    

def derivative(xs: list):
        return [(i * x) for i, x in enumerate(xs)][1:]
    

def fibfib(n: int):
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    

FIX = """
Add more test cases.
"""

def vowels_count(s):
        vowels = "aeiouAEIOU"
        n_vowels = sum(c in vowels for c in s)
        if s[-1] == 'y' or s[-1] == 'Y':
            n_vowels += 1
        return n_vowels
    

def circular_shift(x, shift):
        s = str(x)
        if shift > len(s):
            return s[::-1]
        else:
            return s[len(s) - shift:] + s[:len(s) - shift]
    

def digitSum(s):
        if s == "": return 0
        return sum(ord(char) if char.isupper() else 0 for char in s)
    

def fruit_distribution(s,n):
        lis = list()
        for i in s.split(' '):
            if i.isdigit():
                lis.append(int(i))
        return n - sum(lis)
    

def pluck(arr):
        if(len(arr) == 0): return []
        evens = list(filter(lambda x: x%2 == 0, arr))
        if(evens == []): return []
        return [min(evens), arr.index(min(evens))]
    

def search(lst):
        frq = [0] * (max(lst) + 1)
        for i in lst:
            frq[i] += 1;
    
        ans = -1
        for i in range(1, len(frq)):
            if frq[i] >= i:
                ans = i
        
        return ans
    

def strange_sort_list(lst):
        res, switch = [], True
        while lst:
            res.append(min(lst) if switch else max(lst))
            lst.remove(res[-1])
            switch = not switch
        return res
    

def triangle_area(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return -1 
        s = (a + b + c)/2    
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        area = round(area, 2)
        return area
    

def will_it_fly(q,w):
        if sum(q) > w:
            return False
    
        i, j = 0, len(q)-1
        while i<j:
            if q[i] != q[j]:
                return False
            i+=1
            j-=1
        return True
    

def smallest_change(arr):
        ans = 0
        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - i - 1]:
                ans += 1
        return ans
    

def total_match(lst1, lst2):
        l1 = 0
        for st in lst1:
            l1 += len(st)
        
        l2 = 0
        for st in lst2:
            l2 += len(st)
        
        if l1 <= l2:
            return lst1
        else:
            return lst2
    

def is_multiply_prime(a):
        def is_prime(n):
            for j in range(2,n):
                if n%j == 0:
                    return False
            return True
    
        for i in range(2,101):
            if not is_prime(i): continue
            for j in range(2,101):
                if not is_prime(j): continue
                for k in range(2,101):
                    if not is_prime(k): continue
                    if i*j*k == a: return True
        return False
    

def is_simple_power(x, n):
        if (n == 1): 
            return (x == 1) 
        power = 1
        while (power < x): 
            power = power * n 
        return (power == x) 
    

def iscube(a):
        a = abs(a)
        return int(round(a ** (1. / 3))) ** 3 == a
    

def hex_key(num):
        primes = ('2', '3', '5', '7', 'B', 'D')
        total = 0
        for i in range(0, len(num)):
            if num[i] in primes:
                total += 1
        return total
    

def decimal_to_binary(decimal):
        return "db" + bin(decimal)[2:] + "db"
    

def is_happy(s):
        if len(s) < 3:
          return False
    
        for i in range(len(s) - 2):
          
          if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
        return True
    

def numerical_letter_grade(grades):
    
       
        letter_grade = []
        for gpa in grades:
            if gpa == 4.0:
                letter_grade.append("A+")
            elif gpa > 3.7:
                letter_grade.append("A")
            elif gpa > 3.3:
                letter_grade.append("A-")
            elif gpa > 3.0:
                letter_grade.append("B+")
            elif gpa > 2.7:
                letter_grade.append("B")
            elif gpa > 2.3:
                letter_grade.append("B-")
            elif gpa > 2.0:
                letter_grade.append("C+")
            elif gpa > 1.7:
                letter_grade.append("C")
            elif gpa > 1.3:
                letter_grade.append("C-")
            elif gpa > 1.0:
                letter_grade.append("D+")
            elif gpa > 0.7:
                letter_grade.append("D")
            elif gpa > 0.0:
                letter_grade.append("D-")
            else:
                letter_grade.append("E")
        return letter_grade
    

def prime_length(string):
        l = len(string)
        if l == 0 or l == 1:
            return False
        for i in range(2, l):
            if l % i == 0:
                return False
        return True
    

def starts_one_ends(n):
        if n == 1: return 1
        return 18 * (10 ** (n - 2))
    

def solve(N):
        return bin(sum(int(i) for i in str(N)))[2:]
    

def add(lst):
        return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])
    

def anti_shuffle(s):
        return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])
    

def get_row(lst, x):
        coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
        return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
    

def sort_array(array):
        return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 
    

def encrypt(s):
        d = 'abcdefghijklmnopqrstuvwxyz'
        out = ''
        for c in s:
            if c in d:
                out += d[(d.index(c)+2*2) % 26]
            else:
                out += c
        return out
    

def next_smallest(lst):
        lst = sorted(set(lst))
        return None if len(lst) < 2 else lst[1]
    

def is_bored(S):
        import re
        sentences = re.split(r'[.?!]\s*', S)
        return sum(sentence[0:2] == 'I ' for sentence in sentences)
    

def any_int(x, y, z):
        
        if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
            if (x+y==z) or (x+z==y) or (y+z==x):
                return True
            return False
        return False
    

def encode(message):
        vowels = "aeiouAEIOU"
        vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
        message = message.swapcase()
        return ''.join([vowels_replace[i] if i in vowels else i for i in message])
    

def skjkasdkd(lst):
        def isPrime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
    
            return True
        maxx = 0
        i = 0
        while i < len(lst):
            if(lst[i] > maxx and isPrime(lst[i])):
                maxx = lst[i]
            i+=1
        result = sum(int(digit) for digit in str(maxx))
        return result
    
    

def check_dict_case(dict):
        if len(dict.keys()) == 0:
            return False
        else:
            state = "start"
            for key in dict.keys():
    
                if isinstance(key, str) == False:
                    state = "mixed"
                    break
                if state == "start":
                    if key.isupper():
                        state = "upper"
                    elif key.islower():
                        state = "lower"
                    else:
                        break
                elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                        state = "mixed"
                        break
                else:
                    break
            return state == "upper" or state == "lower" 
    

def count_up_to(n):
        primes = []
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes
    
    

def multiply(a, b):
        return abs(a % 10) * abs(b % 10)
    

def count_upper(s):
        count = 0
        for i in range(0,len(s),2):
            if s[i] in "AEIOU":
                count += 1
        return count
    

def closest_integer(value):
        from math import floor, ceil
    
        if value.count('.') == 1:
            # remove trailing zeros
            while (value[-1] == '0'):
                value = value[:-1]
    
        num = float(value)
        if value[-2:] == '.5':
            if num > 0:
                res = ceil(num)
            else:
                res = floor(num)
        elif len(value) > 0:
            res = int(round(num))
        else:
            res = 0
    
        return res
    
    

def make_a_pile(n):
        return [n + 2*i for i in range(n)]
    

def words_string(s):
        if not s:
            return []
    
        s_list = []
    
        for letter in s:
            if letter == ',':
                s_list.append(' ')
            else:
                s_list.append(letter)
    
        s_list = "".join(s_list)
        return s_list.split()
    

def choose_num(x, y):
        if x > y:
            return -1
        if y % 2 == 0:
            return y
        if x == y:
            return -1
        return y - 1
    

def rounded_avg(n, m):
        if m < n:
            return -1
        summation = 0
        for i in range(n, m+1):
            summation += i
        return bin(round(summation/(m - n + 1)))
    

def unique_digits(x):
        odd_digit_elements = []
        for i in x:
            if all (int(c) % 2 == 1 for c in str(i)):
                odd_digit_elements.append(i)
        return sorted(odd_digit_elements)
    

def by_length(arr):
        dic = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        sorted_arr = sorted(arr, reverse=True)
        new_arr = []
        for var in sorted_arr:
            try:
                new_arr.append(dic[var])
            except:
                pass
        return new_arr
    

def f(n):
        ret = []
        for i in range(1,n+1):
            if i%2 == 0:
                x = 1
                for j in range(1,i+1): x *= j
                ret += [x]
            else:
                x = 0
                for j in range(1,i+1): x += j
                ret += [x]
        return ret
    

def even_odd_palindrome(n):
        def is_palindrome(n):
            return str(n) == str(n)[::-1]
    
        even_palindrome_count = 0
        odd_palindrome_count = 0
    
        for i in range(1, n+1):
            if i%2 == 1 and is_palindrome(i):
                    odd_palindrome_count += 1
            elif i%2 == 0 and is_palindrome(i):
                even_palindrome_count += 1
        return (even_palindrome_count, odd_palindrome_count)
    

def count_nums(arr):
        def digits_sum(n):
            neg = 1
            if n < 0: n, neg = -1 * n, -1 
            n = [int(i) for i in str(n)]
            n[0] = n[0] * neg
            return sum(n)
        return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))
    

def move_one_ball(arr):
        if len(arr)==0:
          return True
        sorted_array=sorted(arr)
        my_arr=[]
        
        min_value=min(arr)
        min_index=arr.index(min_value)
        my_arr=arr[min_index:]+arr[0:min_index]
        for i in range(len(arr)):
          if my_arr[i]!=sorted_array[i]:
            return False
        return True
    

def exchange(lst1, lst2):
        odd = 0
        even = 0
        for i in lst1:
            if i%2 == 1:
                odd += 1
        for i in lst2:
            if i%2 == 0:
                even += 1
        if even >= odd:
            return "YES"
        return "NO"
                
    

def histogram(test):
        dict1={}
        list1=test.split(" ")
        t=0
    
        for i in list1:
            if(list1.count(i)>t) and i!='':
                t=list1.count(i)
        if t>0:
            for i in list1:
                if(list1.count(i)==t):
                    
                    dict1[i]=t
        return dict1
    

def reverse_delete(s,c):
        s = ''.join([char for char in s if char not in c])
        return (s,s[::-1] == s)
    

def odd_count(lst):
        res = []
        for arr in lst:
            n = sum(int(d)%2==1 for d in arr)
            res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
        return res
    

def minSubArraySum(nums):
        max_sum = 0
        s = 0
        for num in nums:
            s += -num
            if (s < 0):
                s = 0
            max_sum = max(s, max_sum)
        if max_sum == 0:
            max_sum = max(-i for i in nums)
        min_sum = -max_sum
        return min_sum
    

def max_fill(grid, capacity):
    import math
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])
    

def sort_array(arr):
        return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
    

def select_words(s, n):
        result = []
        for word in s.split():
            n_consonants = 0
            for i in range(0, len(word)):
                if word[i].lower() not in ["a","e","i","o","u"]:
                    n_consonants += 1 
            if n_consonants == n:
                result.append(word)
        return result
    
    

def get_closest_vowel(word):
        if len(word) < 3:
            return ""
    
        vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
        for i in range(len(word)-2, 0, -1):
            if word[i] in vowels:
                if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                    return word[i]
        return ""
    

def match_parens(lst):
        def check(s):
            val = 0
            for i in s:
                if i == '(':
                    val = val + 1
                else:
                    val = val - 1
                if val < 0:
                    return False
            return True if val == 0 else False
    
        S1 = lst[0] + lst[1]
        S2 = lst[1] + lst[0]
        return 'Yes' if check(S1) or check(S2) else 'No'
    

def maximum(arr, k):
        if k == 0:
            return []
        arr.sort()
        ans = arr[-k:]
        return ans
    

def solution(lst):
        return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])
    

def add_elements(arr, k):
        return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)
    

def get_odd_collatz(n):
        if n%2==0:
            odd_collatz = [] 
        else:
            odd_collatz = [n]
        while n > 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = n*3 + 1
                
            if n%2 == 1:
                odd_collatz.append(int(n))
    
        return sorted(odd_collatz)
    

def valid_date(date):
        try:
            date = date.strip()
            month, day, year = date.split('-')
            month, day, year = int(month), int(day), int(year)
            if month < 1 or month > 12:
                return False
            if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
                return False
            if month in [4,6,9,11] and day < 1 or day > 30:
                return False
            if month == 2 and day < 1 or day > 29:
                return False
        except:
            return False
    
        return True
    

def split_words(txt):
        if " " in txt:
            return txt.split()
        elif "," in txt:
            return txt.replace(',',' ').split()
        else:
            return len([i for i in txt if i.islower() and ord(i)%2 == 0])
    

def is_sorted(lst):
        count_digit = dict([(i, 0) for i in lst])
        for i in lst:
            count_digit[i]+=1 
        if any(count_digit[i] > 2 for i in lst):
            return False
        if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
            return True
        else:
            return False
        
        
    

def intersection(interval1, interval2):
        def is_prime(num):
            if num == 1 or num == 0:
                return False
            if num == 2:
                return True
            for i in range(2, num):
                if num%i == 0:
                    return False
            return True
    
        l = max(interval1[0], interval2[0])
        r = min(interval1[1], interval2[1])
        length = r - l
        if length > 0 and is_prime(length):
            return "YES"
        return "NO"
    

def prod_signs(arr):
        if not arr: return None
        prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
        return prod * sum([abs(i) for i in arr])
    

def minPath(grid, k):
        n = len(grid)
        val = n * n + 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = []
                    if i != 0:
                        temp.append(grid[i - 1][j])
    
                    if j != 0:
                        temp.append(grid[i][j - 1])
    
                    if i != n - 1:
                        temp.append(grid[i + 1][j])
    
                    if j != n - 1:
                        temp.append(grid[i][j + 1])
    
                    val = min(temp)
    
        ans = []
        for i in range(k):
            if i % 2 == 0:
                ans.append(1)
            else:
                ans.append(val)
        return ans
    

def tri(n):
        if n == 0:
            return [1]
        my_tri = [1, 3]
        for i in range(2, n + 1):
            if i % 2 == 0:
                my_tri.append(i / 2 + 1)
            else:
                my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
        return my_tri
    

def digits(n):
        product = 1
        odd_count = 0
        for digit in str(n):
            int_digit = int(digit)
            if int_digit%2 == 1:
                product= product*int_digit
                odd_count+=1
        if odd_count ==0:
            return 0
        else:
            return product
    

def is_nested(string):
        opening_bracket_index = []
        closing_bracket_index = []
        for i in range(len(string)):
            if string[i] == '[':
                opening_bracket_index.append(i)
            else:
                closing_bracket_index.append(i)
        closing_bracket_index.reverse()
        cnt = 0
        i = 0
        l = len(closing_bracket_index)
        for idx in opening_bracket_index:
            if i < l and idx < closing_bracket_index[i]:
                cnt += 1
                i += 1
        return cnt >= 2
    
        
    

def sum_squares(lst):
        import math
        squared = 0
        for i in lst:
            squared += math.ceil(i)**2
        return squared
    

def check_if_last_char_is_a_letter(txt):
     
        check = txt.split(' ')[-1]
        return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False
    

def can_arrange(arr):
        ind=-1
        i=1
        while i<len(arr):
          if arr[i]<arr[i-1]:
            ind=i
          i+=1
        return ind
    

def largest_smallest_integers(lst):
        smallest = list(filter(lambda x: x < 0, lst))
        largest = list(filter(lambda x: x > 0, lst))
        return (max(smallest) if smallest else None, min(largest) if largest else None)
    

def compare_one(a, b):
        temp_a, temp_b = a, b
        if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
        if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
        if float(temp_a) == float(temp_b): return None
        return a if float(temp_a) > float(temp_b) else b 
    

def is_equal_to_sum_even(n):
        return n%2 == 0 and n >= 8
    

def special_factorial(n):
        fact_i = 1
        special_fact = 1
        for i in range(1, n+1):
            fact_i *= i
            special_fact *= fact_i
        return special_fact
    

def fix_spaces(text):
        new_text = ""
        i = 0
        start, end = 0, 0
        while i < len(text):
            if text[i] == " ":
                end += 1
            else:
                if end - start > 2:
                    new_text += "-"+text[i]
                elif end - start > 0:
                    new_text += "_"*(end - start)+text[i]
                else:
                    new_text += text[i]
                start, end = i+1, i+1
            i+=1
        if end - start > 2:
            new_text += "-"
        elif end - start > 0:
            new_text += "_"
        return new_text
    

def file_name_check(file_name):
        suf = ['txt', 'exe', 'dll']
        lst = file_name.split(sep='.')
        if len(lst) != 2:
            return 'No'
        if not lst[1] in suf:
            return 'No'
        if len(lst[0]) == 0:
            return 'No'
        if not lst[0][0].isalpha():
            return 'No'
        t = len([x for x in lst[0] if x.isdigit()])
        if t > 3:
            return 'No'
        return 'Yes'
    

def sum_squares(lst):
        result =[]
        for i in range(len(lst)):
            if i %3 == 0:
                result.append(lst[i]**2)
            elif i % 4 == 0 and i%3 != 0:
                result.append(lst[i]**3)
            else:
                result.append(lst[i])
        return sum(result)
    

def words_in_sentence(sentence):
        new_lst = []
        for word in sentence.split():
            flg = 0
            if len(word) == 1:
                flg = 1
            for i in range(2, len(word)):
                if len(word)%i == 0:
                    flg = 1
            if flg == 0 or len(word) == 2:
                new_lst.append(word)
        return " ".join(new_lst)
    

def simplify(x, n):
        a, b = x.split("/")
        c, d = n.split("/")
        numerator = int(a) * int(c)
        denom = int(b) * int(d)
        if (numerator/denom == int(numerator/denom)):
            return True
        return False
    

def order_by_points(nums):
        def digits_sum(n):
            neg = 1
            if n < 0: n, neg = -1 * n, -1 
            n = [int(i) for i in str(n)]
            n[0] = n[0] * neg
            return sum(n)
        return sorted(nums, key=digits_sum)
    

def specialFilter(nums):
        
        count = 0
        for num in nums:
            if num > 10:
                odd_digits = (1, 3, 5, 7, 9)
                number_as_string = str(num)
                if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                    count += 1
            
        return count 
    

def get_max_triples(n):
        A = [i*i - i + 1 for i in range(1,n+1)]
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (A[i]+A[j]+A[k])%3 == 0:
                        ans += [(A[i],A[j],A[k])]
        return len(ans)
    

def bf(planet1, planet2):
        planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
            return ()
        planet1_index = planet_names.index(planet1)
        planet2_index = planet_names.index(planet2)
        if planet1_index < planet2_index:
            return (planet_names[planet1_index + 1: planet2_index])
        else:
            return (planet_names[planet2_index + 1 : planet1_index])
    

def sorted_list_sum(lst):
        lst.sort()
        new_lst = []
        for i in lst:
            if len(i)%2 == 0:
                new_lst.append(i)
        return sorted(new_lst, key=len)
    

def x_or_y(n, x, y):
        if n == 1:
            return y
        for i in range(2, n):
            if n % i == 0:
                return y
                break
        else:
            return x
    

def double_the_difference(lst):
        return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])
    

def compare(game,guess):
        return [abs(x-y) for x,y in zip(game,guess)]
    

def Strongest_Extension(class_name, extensions):
        strong = extensions[0]
        my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
        for s in extensions:
            val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
            if val > my_val:
                strong = s
                my_val = val
    
        ans = class_name + "." + strong
        return ans
    
    

def cycpattern_check(a , b):
        l = len(b)
        pat = b + b
        for i in range(len(a) - l + 1):
            for j in range(l + 1):
                if a[i:i+l] == pat[j:j+l]:
                    return True
        return False
    

def even_odd_count(num):
        even_count = 0
        odd_count = 0
        for i in str(abs(num)):
            if int(i)%2==0:
                even_count +=1
            else:
                odd_count +=1
        return (even_count, odd_count)
    

def int_to_mini_roman(number):
        num = [1, 4, 5, 9, 10, 40, 50, 90,  
               100, 400, 500, 900, 1000] 
        sym = ["I", "IV", "V", "IX", "X", "XL",  
               "L", "XC", "C", "CD", "D", "CM", "M"] 
        i = 12
        res = ''
        while number: 
            div = number // num[i] 
            number %= num[i] 
            while div: 
                res += sym[i] 
                div -= 1
            i -= 1
        return res.lower()
    

def right_angle_triangle(a, b, c):
        return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b
    

def find_max(words):
        return sorted(words, key = lambda x: (-len(set(x)), x))[0]
    

def eat(number, need, remaining):
        if(need <= remaining):
            return [ number + need , remaining-need ]
        else:
            return [ number + remaining , 0]
    

def do_algebra(operator, operand):
        expression = str(operand[0])
        for oprt, oprn in zip(operator, operand[1:]):
            expression+= oprt + str(oprn)
        return eval(expression)
    

def solve(s):
        flg = 0
        idx = 0
        new_str = list(s)
        for i in s:
            if i.isalpha():
                new_str[idx] = i.swapcase()
                flg = 1
            idx += 1
        s = ""
        for i in new_str:
            s += i
        if flg == 0:
            return s[len(s)::-1]
        return s
    

def string_to_md5(text):
        import hashlib
        return hashlib.md5(text.encode('ascii')).hexdigest() if text else None
    

def generate_integers(a, b):
        lower = max(2, min(a, b))
        upper = min(8, max(a, b))
    
        return [i for i in range(lower, upper+1) if i % 2 == 0]
    