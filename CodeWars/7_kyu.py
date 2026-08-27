# isogram
def is_isogram(string):
    char_set = set()

    for char in string.lower():
        if char in char_set:
            return False
        char_set.add(char)
    
    
    return True



# factorial sums
def sum_factorial(lst):
    result = 0

    for x in lst:
        result += factorial(x)
    
    return result



def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result



def ordered_count(inp):
    char_map = {}
    for char in inp:
        char_map[char] = char_map.get(char, 0) + 1

    return list(char_map.items())

