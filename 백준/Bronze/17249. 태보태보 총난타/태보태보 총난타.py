left_punch, right_punch = input().split('(^0^)')
left_punch = left_punch[::-1]

print(left_punch.count('=@'), right_punch.count('=@'))