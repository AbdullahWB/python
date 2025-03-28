from typing import List, Tuple, Union

n : int = 5 
name : str = "123"
print(type(name))

def sum(a: int, b: int) -> int:
    return a + b


def square_numbers(numbers: List[int]) -> List[int]:
    """Takes a list of integers and returns a list of their squares."""
    return [num ** 2 for num in numbers]

nums = [1, 2, 3, 4]
print(square_numbers(nums))  # Output: [1, 4, 9, 16]


def get_person_info() -> Tuple[str, int, float]:
    """Returns a tuple containing a name, age, and height."""
    return ("Alice", 25, 5.6)

person = get_person_info()
print(person)  # Output: ('Alice', 25, 5.6)


def process_value(value: Union[int, float, str]) -> str:
    """Takes an integer, float, or string and returns a formatted string."""
    if isinstance(value, (int, float)):
        return f"Number: {value}"
    elif isinstance(value, str):
        return f"String: {value}"

print(process_value(10))      # Output: Number: 10
print(process_value(3.14))    # Output: Number: 3.14
print(process_value("Hello")) # Output: String: Hello