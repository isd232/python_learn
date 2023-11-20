import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


# Input the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    # Input regex for each test case
    regex = input()

    # Check if the regex is valid and print the result
    print(is_valid_regex(regex))