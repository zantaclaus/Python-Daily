numbers = []
while True:
    numbers.append(int(input()))
    if numbers[-1] == 0:
        break

sort__type = input()
numbers.sort(reverse=True) if sort__type.lower() == "max" else numbers.sort()

ans = " ".join([str(x) for x in numbers])
print(ans)
