def dot(list1, list2):
    if len(list1) != len(list2):
        return False
    dotProduct = 0
    for i in range(len(list1)):
        dotProduct += list1[i] * list2[i]
    return dotProduct


list1 = [float(x) for x in input().split()]
list2 = [float(x) for x in input().split()]
if dot(list1, list2):
    print(dot(list1, list2))
else:
    print("Error")
