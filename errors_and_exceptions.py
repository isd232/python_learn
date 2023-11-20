def integer_division(a, b):
    try:
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)


num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    a, b = input().split()

    integer_division(a, b)
