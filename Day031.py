from pathlib import Path
path = Path("Day031.txt")

num = int(input())
if num == 1:
    print(path.read_text())
elif num == 2:
    text = input("Write to Text: ")
    text = "".join([letter for letter in text.split()])
    path.write_text(text)
elif num == 3:
    text = input("Update to Text: ")
    text = "".join([letter for letter in text.split()])
    path.write_text(path.read_text() + text)
