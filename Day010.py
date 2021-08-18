numbers = []
numbers.append(int(input()))
while(numbers[-1] != -1):
    numbers.append(int(input()))

for number in numbers:
    if numbers.count(number) >= len(numbers) / 2:
        print(number)
        break
else:
    print("Not found")
