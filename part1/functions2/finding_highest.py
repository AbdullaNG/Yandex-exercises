def find_mountain(heightsMap):
    row = -1
    maxx = 0
    for i in heightsMap:
        if max(i) > maxx:
            maxx = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == maxx:
                return row, column