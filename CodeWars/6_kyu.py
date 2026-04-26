#  multiples of 3 or 5
def solution(number):
    total = 0
    if number < 0:
        return 0
    
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total