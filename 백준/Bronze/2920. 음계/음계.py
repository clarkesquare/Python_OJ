melodies = list(map(str, input().split()))
result = ''

for i in range(1, len(melodies)):
    if melodies[i-1] < melodies[i] and not result == 'descending':
        result = 'ascending'
    elif melodies[i-1] > melodies[i] and not result == 'ascending':
        result = 'descending'
    else:
        result = 'mixed'
        break

print(result)