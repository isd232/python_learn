import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    regex = input()

    print(is_valid_regex(regex))