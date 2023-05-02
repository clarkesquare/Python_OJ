n = int(input())
answer = 0

for _ in range(n):
    numbers = list(map(str, input().split()))
    answer = numbers[0]
    answer = float(answer)

    for i in range(1, len(numbers)):
        if numbers[i] == "@":
            answer *= 3
        elif numbers[i] == "%":
            answer += 5
        elif numbers[i] == "#":
            answer -= 7
    print(format(answer, ".2f"))