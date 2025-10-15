txt = input().split()
i = 0

while len(txt) > 1:
    if txt[i] == '*':
        txt.insert(i - 2, int(txt[i - 2]) * int(txt[i - 1]))
        del txt[i - 1:i + 2]
        i -= 2
    elif txt[i] == '+':
        txt.insert(i - 2, int(txt[i - 2]) + int(txt[i - 1]))
        del txt[i - 1:i + 2]
        i -= 2
    elif txt[i] == '-':
        txt.insert(i - 2, int(txt[i - 2]) - int(txt[i - 1]))
        del txt[i - 1:i + 2]
        i -= 2
    else:
        i += 1

print(txt[0])