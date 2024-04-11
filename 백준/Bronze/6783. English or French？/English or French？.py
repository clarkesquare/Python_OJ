word = ""
cnt = [0, 0]

for _ in range(int(input())):
    word = input().lower()
    cnt[0] += word.count("t")
    cnt[1] += word.count("s")

print("French" if cnt[0] <= cnt[1] else "English")