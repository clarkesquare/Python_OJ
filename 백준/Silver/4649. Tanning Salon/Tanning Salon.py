while True:
    word = input()
    if word != "0":
        n, pattern = word.split()
        n = int(n)
        temp = []
        passed = []
        for i in pattern:
            if i not in temp:
                if len(temp) < n:
                    temp.append(i)
                else:
                    if i not in passed:
                        passed.append(i)
            
            else:
                temp.remove(i)

        if len(passed) != 0:
            print(f"{len(passed)} customer(s) walked away.")
    
        else:
            print("All customers tanned successfully.")
    
    else:
        break