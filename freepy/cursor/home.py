"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return first is second


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise TypeError
    Raises:
        TypeError
    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(first_value) == int and type(second_value) == int:
        return first_value * second_value
    else:
        raise TypeError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError
    Args:
        first_value: number for multiply
        second_value: number for multiply
    Raises:
        ValueError
    Returns: multiple of two numbers.
    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
        first = int(first_value)
        second = int(second_value)
    except ValueError:
        raise ValueError
    return first * second


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.
    Args:
        word: Searchable substring
        text: Text for search
    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False
    """
    return word in text.split()


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    return [i for i in range(13) if i != 6 and i != 7]


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    return [i for i in data if i >= 0]


def alphabet() -> dict:
    """
    Create dict which keys are alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    from string import ascii_lowercase
    return {i: j for i, j in enumerate(ascii_lowercase, start=1)}


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    """
    swap = True
    while swap:
        swap = False
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1],data[i]
                swap = True
    return data

# These "asserts" using only for self-checking and not necessary
if __name__ == '__main__':
#    assert is_two_object_has_same_value(["Hello", 15, True], ("Hello", 15, True)) is True #НЕ знаю що з цим робити
    assert is_two_objects_is_the_same_objects(96, 96.0) is False
    assert is_two_objects_is_the_same_objects(["Hello", 15, True], ["Hello", 15, True]) is True
    assert is_two_objects_is_the_same_objects(["Hello", 15, True], ("Hello", 15, True)) is False
    assert multiple_ints(10, 10) == 100
#    multiple_ints(6.0, 2)
#    multiple_ints([12, 5, 7], 2)
#    multiple_ints("Some useful text from from your teacher", 2)
#    multiple_ints(True, 2)
    assert multiple_ints_with_conversion(6, 0) == 0
    assert multiple_ints_with_conversion(12, 2) == 24
    assert multiple_ints_with_conversion("12", "2") == 24
    multiple_ints_with_conversion("Some useful text from your teacher", 2)
    assert is_word_in_text("This", "This is very easy task") is True
    assert is_word_in_text("None", "This is very easy task") is False
    assert some_loop_exercise() == [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12]
    assert remove_from_list_all_negative_numbers([-14, -59, -36, -69, -73, -69, -44, -83, -77, -93]) == []
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                'x': 24, 'y': 25, 'z': 26}
    assert alphabet() == expected
    import random
    for _ in range(10):
        given_data = [random.randint(0, 100) for x in range(random.randint(2, 20))]
        expected_result = given_data.copy()
    assert simple_sort(given_data) == sorted(expected_result)
    print("Hello")