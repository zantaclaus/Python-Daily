def insert(lists):
    ans = []
    for index, x in enumerate(lists):
        if index % 2 != 0:
            ans.insert(0, x)
        else:
            ans.append(x)
    return ans


numbers = []
n = int(input())
for i in range(n):
    numbers.append(int(input()))
for x in input().split():
    numbers.append(int(x))
while True:
    x = int(input())
    if x != -1:
        numbers.append(x)
    else:
        break
print(insert(numbers))
