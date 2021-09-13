def union(lists):
    ans = []
    for items in lists:
        ans += items
    return set(ans)


def intersect(n, lists):
    ans = []
    for item in lists[0]:
        for i in range(1, n):
            if item not in lists[i]:
                break
        else:
            ans.append(item)
    return ans


n = int(input())
lists = []
for i in range(n):
    inputs = input().split()
    lists.append(set(inputs))

print(len(union(lists)))
print(len(intersect(n, lists)))
