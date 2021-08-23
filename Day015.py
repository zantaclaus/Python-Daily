import math


def factorial(x):
    return 1 if x == 1 or x == 0 else x * factorial(x-1)


n = int(input())
ans = 0
for i in range(1, int(math.ceil(n/2)) + 1):
    lst = []
    count2 = 0
    for j in range(1, i):
        if sum(lst) + 2 < n:
            lst.append(2)
            count2 += 1
    count1 = 0
    while(sum(lst) < n):
        lst.append(1)
        count1 += 1
    ans += factorial(len(lst))/(factorial(count2)*factorial(count1))

if n % 2 == 0:
    print(ans + 1)
else:
    print(ans)
