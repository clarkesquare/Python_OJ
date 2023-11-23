n = 0
name1, name2 = [], []
answer = []

while True:
    n += 1
    name1, name2 = [], []
    answer = []
    number = int(input())
    if number != 0:
        for i in range(number):
            if i % 2 == 0:
                name1.append(input())
            else:
                name2.append(input())
        
        answer = name1 + name2[::-1]
        print('SET', n)
        for j in answer:
            print(j)

    else:
        break