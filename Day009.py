A = int(input("Input A: "))
for i in range(5):
    B = int(input("input B: "))
    if B > A:
        print("Higher")
    elif B < A:
        print("Lower")
    else:
        print("You Win")
        break
else:
    print("You Lose")
