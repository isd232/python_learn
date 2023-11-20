if __name__ == '__main__':
    # Input the number of scores
    n = int(input())

    # Input the list of scores as integers
    arr = map(int, input().split())

    # Remove duplicates and sort the scores in descending order
    unique_sorted_scores = sorted(set(arr), reverse=True)

    # The second element in the sorted list is the runner-up score
    runner_up_score = unique_sorted_scores[1]

    # Print the result
    print("The runner-up score is:", runner_up_score)
