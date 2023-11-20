def is_leap(year):
    # By default, assume the year is not a leap year
    leap = False

    # Check if the year is divisible by 4 and not divisible by 100,
    # or if it is divisible by 400. If either condition is true, it's a leap year.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True  # Set leap to True if the conditions are met

    # Return the final result (True for leap year, False otherwise)
    return leap

# Get input from the user for the year
year = int(input())

# Call the function and print the result
print(is_leap(year))
