st = int(input())
n = 1
ter = 0
right = 0
while ter != st:
    num = input()
    if n == 1 and num == "раз":
        right += 1
        n += 1
    elif n == 2 and num == "два":
        right += 1
        n += 1
    elif n == 3 and num == "три":
        right += 1
        n += 1
    elif n == 4 and num == "четыре":
        right += 1
        n = 1
    else:
        print(f"Правильных отсчётов было {right}, но теперь вы ошиблись.")
        right = 0
        ter += 1
        n = 1
print("На сегодня хватит.")