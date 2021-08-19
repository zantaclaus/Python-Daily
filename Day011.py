x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))
if y > x:
    x, y = y, x
for i in range(x, 1, -1):
    if x % i == 0 and y % i == 0:
        print(f"Greatest commom divisor = {i}")
        break
