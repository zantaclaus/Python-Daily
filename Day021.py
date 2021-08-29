def fact(x):
    return 1 if x == 1 or x == 0 else x*fact(x-1)


numbers = [int(x) for x in input().split()]
print([fact(x) for x in numbers])
