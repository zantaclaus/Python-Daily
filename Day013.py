def isSubset(list1, list2):
    for number in list1:
        if number not in list2:
            break
    else:
        return True

    for number in list2:
        if number not in list1:
            return False
    else:
        return True


numbers = [str(x) for x in range(0, 10)]
input1, input2 = input().split(", ")
list1 = [x for x in input1 if x in numbers]
list2 = [x for x in input2 if x in numbers]
print(isSubset(list1, list2))
