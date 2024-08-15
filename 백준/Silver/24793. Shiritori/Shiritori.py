import sys

input = sys.stdin.readline

pattern = {}
word = ""
tmp = ""
answer = "Fair Game"

for i in range(int(input())):
    word = input().strip()
    if tmp != "game over":
        if i == 0: # 최초 셋팅
            tmp = word
            pattern[tmp] = ""
        
        else: # 2회차 부터 검사 진행
            if word[0] != tmp[-1] or word in pattern:
                tmp = "game over"
            
            else:
                pattern[word] = ""
                tmp = word

        if tmp == "game over": # 게임 오버
            answer = "Player 1 lost" if i % 2 == 0 else "Player 2 lost"
    
print(answer)