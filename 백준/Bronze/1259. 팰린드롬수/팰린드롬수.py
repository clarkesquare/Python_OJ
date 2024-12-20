while True:
    pattern = input()
    if pattern != "0":
        if pattern == pattern[::-1]:
            print("yes")
        
        else:
            print("no")
    
    else:
        break