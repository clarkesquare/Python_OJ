bools = list(input().split())

if bools[1] == 'AND':
    if bools[0] == 'true' and bools[2] == 'true':
        print('true')
    else:
        print('false')

elif bools[1] == 'OR':
    if bools[0] == 'false' and bools[2] == 'false':
        print('false')
    else:
        print('true')