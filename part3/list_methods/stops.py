stops = [int(j) for j in input().split()]
stop = [int(i) for i in input().split()]
x = sum(stops[stop[0]:stop[1]])
print(x)