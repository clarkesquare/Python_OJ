x, y = map(int, input().split())

dotw = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answewr = dotw[0]

y += sum(day[:x-1])

print(dotw[y % 7])