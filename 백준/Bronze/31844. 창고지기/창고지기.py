pattern = input()

robot = pattern.index("@")
box = pattern.index("#")
place = pattern.index("!")
answer = 0

if (robot < box and box < place) or (robot > box and box > place):
    answer = abs(place - robot) -1
else:
    answer = -1

print(answer)