def integer_division(a, b):
    try:
        # Attempt to perform integer division
        result = int(a) // int(b)

        # Print the result if successful
        print(result)

    except ZeroDivisionError as e:
        # Handle the case where division by zero occurs
        print("Error Code:", e)


# Input the number of test cases
num_of_test_cases = int(input())

# Iterate through each test case
for _ in range(num_of_test_cases):
    # Input two space-separated numbers for each test case
    a, b = input().split()

    # Call the function for integer division and handle exceptions
    integer_division(a, b)
