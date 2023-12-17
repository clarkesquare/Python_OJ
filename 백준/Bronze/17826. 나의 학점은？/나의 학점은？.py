scores = map(int, input().split())
answer = ''

scores = sorted(scores, reverse=True)
hongik = scores.index(int(input())) + 1

if 1 <= hongik and hongik <= 5:
    answer = 'A+'
elif hongik <= 15:
    answer = 'A0'
elif hongik <= 30:
    answer = 'B+'
elif hongik <= 35:
    answer = 'B0'
elif hongik <= 45:
    answer = 'C+'
elif hongik <= 48:
    answer = 'C0'
else:
    answer = 'F'

print(answer)