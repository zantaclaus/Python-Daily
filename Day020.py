lists1 = []
lists2 = []

n = int(input())
for i in range(n):
    point = [int(x) for x in input().split()]
    if i % 2 == 0:
        lists1.append(point[0])
        lists2.append(point[1])
    else:
        lists1.append(point[1])
        lists2.append(point[0])


if input() == "Zig-Zag":
    print(f"Output: {min(lists1)} {max(lists2)}")
else:
    print(f"Output: {min(lists2)} {max(lists1)}")
