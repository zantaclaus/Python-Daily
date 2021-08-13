def isSame(numbers):
    for number in numbers:
        if numbers.count(number) > 1:
            return True
    return False


numbers = [int(x) for x in input()]
print(isSame(numbers))
