def solution(nums):
    answer = 0
    temp = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                temp = 0
                for l in range(2, nums[i]+nums[j]+nums[k]):
                    if (nums[i]+nums[j]+nums[k]) % l == 0:
                        temp = 1
                        break
                if temp == 0:
                    answer += 1

    return answer