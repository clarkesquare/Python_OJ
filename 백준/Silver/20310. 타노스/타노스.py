word = input()
answer = [word.count("0")//2, word.count("1")//2]

print("0" * answer[0] + "1" * answer[1])