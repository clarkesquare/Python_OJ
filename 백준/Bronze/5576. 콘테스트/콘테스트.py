list1 = []
list2 = []

for _ in range(10):
    list1.append(int(input()))

for _ in range(10):
    list2.append(int(input()))

list1.sort()
list2.sort()

print(sum(list1[-3::]), sum(list2[-3::]))