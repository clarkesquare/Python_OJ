for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = int(input())
    subject = []
    verb = []
    object = []
    for _ in range(a):
        subject.append(input())
    
    for _ in range(b):
        verb.append(input())
    
    for _ in range(c):
        object.append(input())
    
    for i in subject:
        for j in verb:
            for k in object:
                print(f"{i} {j} {k}.")
    
    print()