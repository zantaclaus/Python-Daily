def isLeapYear(num):
    if num % 4 != 0:
        return False
    if num % 100 != 0:
        return True
    if num % 400 != 0:
        return False
    return True


day = int(input("Input day: "))
month = int(input("Input month: "))
year = int(input("Input year: ")) - 543
days = 0

if isLeapYear(year):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month - 1):
    days += months[i]

days += day
print("A day of year:", days)
