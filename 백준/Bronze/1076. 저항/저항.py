resist_one = input()
resist_two = input()
resist_three = input()
resist = ''

if resist_one == 'black':
    resist += '0'
elif resist_one == 'brown':
    resist += '1'
elif resist_one == 'red':
    resist += '2'
elif resist_one == 'orange':
    resist += '3'
elif resist_one == 'yellow':
    resist += '4'
elif resist_one == 'green':
    resist += '5'
elif resist_one == 'blue':
    resist += '6'
elif resist_one == 'violet':
    resist += '7'
elif resist_one == 'grey':
    resist += '8'
elif resist_one == 'white':
    resist += '9'

if resist_two == 'black':
    resist += '0'
elif resist_two == 'brown':
    resist += '1'
elif resist_two == 'red':
    resist += '2'
elif resist_two == 'orange':
    resist += '3'
elif resist_two == 'yellow':
    resist += '4'
elif resist_two == 'green':
    resist += '5'
elif resist_two == 'blue':
    resist += '6'
elif resist_two == 'violet':
    resist += '7'
elif resist_two == 'grey':
    resist += '8'
elif resist_two == 'white':
    resist += '9'

if resist_three == 'black':
    resist = int(resist) * ( 10 ** 0 )
elif resist_three == 'brown':
    resist = int(resist) * ( 10 ** 1 )
elif resist_three == 'red':
    resist = int(resist) * ( 10 ** 2 )
elif resist_three == 'orange':
    resist = int(resist) * ( 10 ** 3 )
elif resist_three == 'yellow':
    resist = int(resist) * ( 10 ** 4 )
elif resist_three == 'green':
    resist = int(resist) * ( 10 ** 5 )
elif resist_three == 'blue':
    resist = int(resist) * ( 10 ** 6 )
elif resist_three == 'violet':
    resist = int(resist) * ( 10 ** 7 )
elif resist_three == 'grey':
    resist = int(resist) * ( 10 ** 8 )
elif resist_three == 'white':
    resist = int(resist) * ( 10 ** 9 )

print(resist)