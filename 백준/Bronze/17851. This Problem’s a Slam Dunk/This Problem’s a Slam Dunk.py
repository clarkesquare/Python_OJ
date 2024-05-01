state_u = []
u_state = []
answer = 0

state_u = list(map(int, input().split()))
u_state = list(map(int, input().split()))

state_u.sort()
u_state.sort()

for i in range(5):
    if state_u[i] > u_state[i]:
        answer += 1

print(answer)