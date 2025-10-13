from collections import deque

def solution(priorities, location):
    process = deque(sorted(priorities, reverse=True))
    priorities = deque(priorities)
    count = 0
    end = 0

    while True:
        count += 1
        for i in range(len(priorities)):
            if process[0] == priorities[0]:
                if location != 0:
                    location -= 1
                    process.popleft()
                    priorities.popleft()

                else:
                    end = 1

                break

            else:
                priorities.append(priorities.popleft())
                if location == 0:
                    location += len(priorities) - 1

                else:
                    location -= 1

        if end == 1:
            break
            
    return count