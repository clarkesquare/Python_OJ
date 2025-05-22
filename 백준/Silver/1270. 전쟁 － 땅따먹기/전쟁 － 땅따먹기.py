n = int(input())

for _ in range(n):
    area = {}
    answer = []
    numbers = list(map(int, input().split()))
    if numbers[0] != 0:
        if numbers[0] != 1:
            for i in range(1, numbers[0] + 1):
                if numbers[i] not in area:
                    area[numbers[i]] = 1
                
                else:
                    area[numbers[i]] += 1

            answer = list(area.items())
            if len(area) != 1:
                answer.sort(key = lambda x:x[1], reverse=True)
                if answer[0][1] == answer[1][1] or answer[0][1] <= ((len(numbers) - 1) / 2):
                    print('SYJKGW')
                
                else:
                    print(answer[0][0])
            
            else:
                print(answer[0][0])
        
        else:
            print(numbers[1])