if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_sorted_scores = sorted(set(arr), reverse=True)

    runner_up_score = unique_sorted_scores[1]

    print("The runner-up score is:", runner_up_score)