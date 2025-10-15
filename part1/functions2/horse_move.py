def possible_turns(cell):
    allwd = [(-1, 2), (-2, 1), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    char = 'ABCDEFGH'
    lt = []
    y = int(cell[1])
    x = char.find(cell[0]) + 1
    for xy in allwd:
        x1 = x + xy[0]
        y1 = y + xy[1]
        if 0 < x1 < 9 and 0 < y1 < 9:
            lt.append(char[x1 - 1] + str(y1))
    lt.sort()
    return lt