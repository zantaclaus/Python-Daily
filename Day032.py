deg = 90
n = int(input("Input num: "))
string = []
print("Input String : ")
for i in range(n):
    string.append(input())

check = len(string[0])
for word in string:
    if len(word) != check:
        print("Invalid size")
        break
else:
    string = string[::-1]
    ans = []
    for i in range(check):
        temp = ""
        for word in string:
            temp += word[i]
        ans.append(temp)
    print(ans)
