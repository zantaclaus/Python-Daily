def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input("Input number: "))
ans = []
while True:
    if isPrime(n):
        ans.append(n)
    if len(ans) == 2:
        if ans[1] - ans[0] == 2:
            print(f"Next twin prime: {ans[0]},{ans[1]}")
            break
        else:
            ans.pop(0)
    n += 1
