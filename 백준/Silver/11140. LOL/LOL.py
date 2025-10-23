for _ in range(int(input())):
    word = input()
    if 'lol' in word:
        answer = 0
    
    else:
        if 'lo' in word:
            answer = 1
        
        elif 'ol' in word:
            answer = 1
        
        elif 'll' in word:
            answer = 1
        
        elif 'l' in word:
            for i in range(len(word) - 2):
                if word[i] == 'l' and word[i+2] == 'l':
                    answer = 1
                    break

            else:
                answer = 2
        
        elif 'o' in word:
            answer = 2
        
        else:
            answer = 3

    print(answer)