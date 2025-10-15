x_klad = int(input())
y_klad = int(input())
x = 0
y = 0
c = 0
z = 1
while True:
    if (x == x_klad) and (y == y_klad):
        break
    else:
        a = input()
        if a == "вперёд":
            b = int(input())
            if z == 1:
                y += b
            elif z == 3:
                y -= b
            elif z == 2:
                x += b
            elif z == 4:
                x -= b
            c += 1
        elif a == "направо":
            if z == 4:
                z = 1
            else:
                z += 1
            c += 1
        elif a == "налево":
            if z == 1:
                z = 4
            else:
                z -= 1
            c += 1
        elif a == "разворот":
            if (z == 3) or (z == 4):
                z -= 2
            else:
                z += 2
            c += 1
print(c)
if z == 1:
    print("север")
elif z == 2:
    print("восток")
elif z == 3:
    print("юг")
elif z == 4:
    print("запад")