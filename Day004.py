numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inputs = [int(x) for x in input()]
numbers_pop = [x for x in numbers if x not in inputs]

if len(numbers_pop) == 0:
    print("None")
else:
    ans = " ".join(str(x) for x in numbers_pop)
    print(ans)
