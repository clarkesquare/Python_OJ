pattern = {'cs': ['Kamen', 'Nuzky', 'Papir'], 'en': ['Rock', 'Scissors', 'Paper'],
            'fr': ['Pierre', 'Ciseaux', 'Feuille'], 'de': ['Stein', 'Schere', 'Papier'],
            'hu': ['Ko', 'Ollo', 'Papir'], 'it': ['Sasso', 'Forbice', 'Carta'],
            'jp': ['Guu', 'Choki', 'Paa'], 'pl': ['Kamien', 'Nozyce', 'Papier'],
            'es': ['Piedra', 'Tijera', 'Papel']}
# 'hu' Ko || Koe, Ollo | Olloo, Papier
# 'it' Sasso | Roccia, Forbice, Carta | Rete
cnt = 0

while True:
    cnt += 1
    a, b = input().split()
    c, d = input().split()
    scores = [0, 0]
    
    while True:
        tmp = input()
        if tmp == '-':
            break

        elif tmp == '.':
            break

        else:
            e, f = tmp.split()

            if a == 'hu': # 헝가리 패턴 걸러내기
                if e == 'Koe':
                    e = 'Ko'
                
                if e == 'Olloo':
                    e = 'Ollo'
            
            if c == 'hu':
                if f == 'Koe':
                    f = 'Ko'
                
                if f == 'Olloo':
                    f = 'Ollo'

            if a == 'it': # 이탈리아 패턴 걸러내기
                if e == 'Roccia':
                    e = 'Sasso'

                if e == 'Rete':
                    e = 'Carta'

            if c == 'it':
                if f == 'Roccia':
                    f = 'Sasso'

                if f == 'Rete':
                    f = 'Carta'

            e, f = pattern[a].index(e), pattern[c].index(f)
            if e == f:
                continue
            
            if e == 0: # 묵 찌 빠
                if f == 1:
                    scores[0] += 1
                
                elif f == 2:
                    scores[1] += 1
            
            elif e == 1:
                if f == 0:
                    scores[1] += 1
                
                elif f == 2:
                    scores[0] += 1
            
            else:
                if f == 0:
                    scores[0] += 1
                
                else:
                    scores[1] += 1
    
    print(f'Game #{cnt}:')
    if scores[0] != 1:
        print(f'{b}: {scores[0]} points')
    
    else:
        print(f'{b}: {scores[0]} point')
    
    if scores[1] != 1:
        print(f'{d}: {scores[1]} points')
    
    else:
        print(f'{d}: {scores[1]} point')

    if scores[0] > scores[1]:
        print(f'WINNER: {b}')
    
    elif scores[0] < scores[1]:
        print(f'WINNER: {d}')
    
    else:
        print('TIED GAME')
    
    if tmp == '.':
        break

    else:
        print()