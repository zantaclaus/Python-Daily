def nextPrime(num):
    while True:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            return num


num = int(input())
print(nextPrime(num))
