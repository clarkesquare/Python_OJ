first = list(input().split())
second = list(input().split())
answer = 0

if "BC" in first:
    first[0] = int(first[0])
    if "BC" in second:
        second[0] = int(second[0])
        answer = max(first[0], second[0]) - min(first[0], second[0])
    else:
        second[1] = int(second[1])
        answer = first[0] + second[1] - 1

else:
    first[1] = int(first[1])
    if "BC" in second:
        second[0] = int(second[0])
        answer = first[1] + second[0] - 1
    else:
        second[1] = int(second[1])
        answer = max(first[1], second[1]) - min(first[1], second[1])

print(answer)