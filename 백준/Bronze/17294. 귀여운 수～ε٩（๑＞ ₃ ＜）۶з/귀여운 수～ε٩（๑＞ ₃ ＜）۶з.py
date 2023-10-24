n = input()
answer = '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'

if len(n) != 1:
    pattern = int(n[1]) - int(n[0])
    for i in range(2, len(n)):
        if int(n[i]) - int(n[i-1]) != pattern:
            answer = '흥칫뿡!! <(￣ ﹌ ￣)>'
            break

print(answer)