n = input()

[print(n[i:len(n) - i]) for i in range(len(n) // 2 + 1)]