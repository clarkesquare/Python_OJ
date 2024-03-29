a = ''
b = ''
c = ''
numbers = ''

while True:
    numbers = input()
    if numbers != "0+0=0":
        a, b = numbers.split("+")
        b, c = b.split("=")
        a, b, c = a[::-1], b[::-1], c[::-1]
        print("True" if int(a) + int(b) == int(c) else "False")

    else:
        print("True")
        break