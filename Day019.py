h = int(input("Enter high (Metre) : "))
i = 1
while h >= 0.1:
    h *= 0.9
    print(f"[z#{i}] High : {h:.2f}")
    i += 1
print(f"Hit count : {i-1}")
