answer = 0

for i in range(3):
    n = input()
    if n.isnumeric() and answer == 0:
        answer = int(n) + (3 - i)


if answer % 3 == 0 and answer % 5 == 0:
    print("FizzBuzz")

elif answer % 3 == 0:
    print("Fizz")

elif answer % 5 == 0:
    print("Buzz")

else:
    print(answer)