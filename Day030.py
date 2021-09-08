num = int(input())
ans = []
for i in range(1, num):
    for j in range(1, i):
        for k in range(1, i):
            if i**2 == j**2 + k**2 and num == i + j + k:
                ans.append(i)
print(max(ans))
