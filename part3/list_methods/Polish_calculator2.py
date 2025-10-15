txt = input().split()
i = 0
f = 1

while len(txt) > 1:
    if txt[i] == '*':
        txt.insert(i - 2, int(txt[i - 2]) * int(txt[i - 1]))
        del txt[i - 1:i + 2]
        i -= 2
    elif txt[i] == '/':
        txt.insert(i - 2, int(txt[i - 2]) // int(txt[i - 1]))
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
    elif txt[i] == '#':
        txt.insert(i, int(txt[i - 1]))
        del txt[i + 1]
        i += 1
    elif txt[i] == '@':
        txt[i - 2], txt[i - 1] = txt[i - 1], txt[i - 2]
        txt[i - 3], txt[i - 1] = txt[i - 1], txt[i - 3]
        del txt[i]
    elif txt[i] == '~':
        txt[i - 1] = int(txt[i - 1]) * -1
        del txt[i]
    elif txt[i] == '!':
        for j in range(1, int(txt[i - 1]) + 1):
            f *= j
        txt[i - 1] = f
        del txt[i]
        f = 1
    else:
        i += 1

print(txt[0])