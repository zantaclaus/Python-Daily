p1, p2, p3, n1, n2 = [int(x) for x in input().split()]
ans = 0

if p1 >= n1 and p1 <= n2:
    ans += 10000

count_2digit = (n2 // 100) - (n1 // 100) - 1
if p2 >= n1 % 100:
    count_2digit += 1
if p2 <= n2 % 100:
    count_2digit += 1
ans += count_2digit * 25

count_3digit = (n2 // 1000) - (n1 // 1000) - 1
if p3 >= n1 % 1000:
    count_3digit += 1
if p3 <= n2 % 1000:
    count_3digit += 1
ans += count_3digit * 100

print(ans)
