if __name__ == '__main__':
    # Input the maximum value for x
    x = int(input())

    # Input the maximum value for y
    y = int(input())

    # Input the maximum value for z
    z = int(input())

    # Input the target sum value
    n = int(input())

    # Generate all possible coordinates within the given ranges
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    # Filter out coordinates where the sum is equal to the target value
    filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

    # Print the filtered coordinates
    print(filtered_coordinates)
