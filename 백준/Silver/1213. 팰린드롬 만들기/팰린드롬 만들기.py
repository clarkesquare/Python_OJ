from string import ascii_uppercase

dictionary = {}
cnt = ""
answer = ""

for i in ascii_uppercase:
    dictionary[i] = 0

for j in input():
    dictionary[j] += 1

for k, v in dictionary.items():
    if v != 0:
        if v % 2 != 0:
            if cnt == "":
                cnt = k
                answer += k * (v//2)
            
            else:
                cnt += cnt
                break
        
        else:
            answer += k * (v//2)

if len(cnt) == 2:
    print("I'm Sorry Hansoo")

elif len(cnt) == 1:
    print(answer + cnt + answer[::-1])

else:
    print(answer + answer[::-1])