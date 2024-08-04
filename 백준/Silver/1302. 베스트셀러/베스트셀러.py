books = {}

for _ in range(int(input())):
    tmp = input()
    if tmp not in books:
        books[tmp] = 1
        
    else:
        books[tmp] += 1

books = dict(sorted(books.items(), key= lambda x: x[0]))
books = sorted(books.items(), key= lambda x: x[1], reverse=True)

print(books[0][0])