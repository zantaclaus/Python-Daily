def isSquare(lists):
    return sorted([number for number in lists if int(number**(1/2)) == number**(1/2)])


print(isSquare([81, 4, 1, 5]))
