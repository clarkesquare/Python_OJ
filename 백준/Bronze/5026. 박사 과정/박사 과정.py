for _ in range(int(input())):
    answer = 0
    question = input()
    if question == 'P=NP':
        print('skipped')
    else:
        question = list(map(int, question.split('+')))
        answer = sum(question)
        print(answer)