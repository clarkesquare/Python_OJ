word = input()

if len(word) >= 5 and word[-5::] == 'driip':
    print('cute')
else:
    print('not cute')