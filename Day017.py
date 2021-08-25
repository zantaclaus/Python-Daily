def findSum100(numbers):
    for index1, number1 in enumerate(numbers):
        for index2, number2 in enumerate(numbers):
            if index1 != index2:
                if sum(numbers) - number1 - number2 == 100:
                    numbers.remove(number1)
                    numbers.remove(number2)
                    return numbers
    return "None"


numbers = [int(x) for x in input().split()]
print(findSum100(numbers))
