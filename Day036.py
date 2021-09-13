m = int(input())
count1 = 0
count2 = 0
for i in range(m * 3):
    player1, player2 = input().split()
    if player1 == "R":
        if player2 == "S":
            count1 += 1
        elif player2 == "P":
            count2 += 1
    elif player1 == "S":
        if player2 == "P":
            count1 += 1
        elif player2 == "R":
            count2 += 1
    elif player1 == "P":
        if player2 == "R":
            count1 += 1
        elif player2 == "S":
            count2 += 1
    if count1 == m or count2 == m:
        print("Output:")
        print(count1, count2)
        if count1 > count2:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break
else:
    print(count1, count2)
    print("Tie")
