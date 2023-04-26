n = int(input())

guests = list(map(int, input().split()))
seats = []
refuses = 0

for i in guests:
    if (i in seats) or (len(seats) >= n):
        refuses += 1
    else:
        seats.append(i)

print(refuses)