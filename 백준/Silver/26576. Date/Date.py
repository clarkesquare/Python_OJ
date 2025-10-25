months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05',
          'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11',
          'December': '12'}

for _ in range(int(input())):
    a, b, c = input().split()
    b = b.strip(',')
    if a in months and (1 <= int(b) and int(b) <= 31):
        if len(b) == 1:
            b = '0' + b
        
        if len(c) == 1:
            c = '0' + c

        print(months[a] + '/' + b + '/' + c[-2:])
    
    else:
        print('Invalid')