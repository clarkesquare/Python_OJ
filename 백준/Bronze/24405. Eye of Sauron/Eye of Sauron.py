sauron = input()

print("correct" if sauron.index("(") == sauron[::-1].index(")") else "fix")