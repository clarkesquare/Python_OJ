from collections import deque

chk = {'(': ')', '{': '}', '[': ']'}
rev_chk = {')': '(', '}': '{', ']': '['}

word = deque(input())
stack = deque()
front = deque()
back = deque()
err = 0

for ch in word:
    if len(stack) == 0:
        if ch in rev_chk:
            front.appendleft(rev_chk[ch])

        else:
            stack.append(ch)

    else:
        if ch in chk:
            stack.append(ch)

        elif chk[stack[-1]] == ch:
            stack.pop()

        else:
            err = 1
            break

# 남은 스택 처리
while stack:
    back.append(chk[stack.pop()])

# 안전하게 list 변환 후 출력
if err == 0:
    print(''.join(list(front) + list(word) + list(back)))
   
else:
    print('NIE')