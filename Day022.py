number = input()
time = 10
summing = 0
for digit in number:
    summing += int(digit) * time
    time -= 1
while summing > 11:
    summing -= 11
print(number + str(11 - summing))
