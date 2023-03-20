colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

resist_one = colors.index(input())
resist_two = colors.index(input())
resist_three = colors.index(input())

resist = int(str(resist_one) + str(resist_two)) * ( 10 ** resist_three )

print(resist)