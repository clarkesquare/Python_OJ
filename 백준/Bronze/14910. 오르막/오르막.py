numbers = list(map(int,input().split()))

print('Good' if numbers == sorted(numbers) else 'Bad')