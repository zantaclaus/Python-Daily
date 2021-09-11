from pathlib import Path
path = Path("Day034.txt")

player = input("Enter score, name : ").split()
scoreboard = [player.split() for player in path.read_text().split("\n")]
for i in range(5):
    if int(scoreboard[i][0]) <= int(player[0]):
        scoreboard.insert(i, player)
        break
ans = "\n".join([scoreboard[i][0] + " " + scoreboard[i][1] for i in range(5)])
path.write_text(ans)
