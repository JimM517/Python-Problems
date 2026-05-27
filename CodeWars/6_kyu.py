#  multiples of 3 or 5
def solution(number):
    total = 0
    if number < 0:
        return 0
    
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total






# unique in order
def unique_in_order(sequence):
    result = []
    prev = None

    for char in sequence:
        if char != prev:
            result.append(char)
            prev = char
    
    return result





# split strings
def split_solution(s):
    if len(s) % 2 != 0:
        s += "_"

    return [s[i:i+2] for i in range(0, len(s), 2)]

    





    