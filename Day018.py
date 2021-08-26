def countUpper(string):
    uppers = [chr(x) for x in range(65, 91)]
    count = 0
    for letter in string:
        if letter in uppers:
            count += 1
    return count


print(countUpper(input()))
