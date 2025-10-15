'''x = input()
y = 0
while x != '!':
    if int(x) > 150 and int(x) < 190:
        y += 1
    x = input()
print(y)'''



y = 0
min_y = 190
max_y = 150
x = input()
while x != '!':
    x = int(x)
    if x >= 150 and x <= 190:
        y += 1
        if x < min_y:
            min_y = x
        if x > max_y:
            max_y = x
    x = input()
print(y)
print(min_y, max_y)