money = int(input())
animals = int(input())

for c in range(1, money // 20 + 1):
    
    for x in range((money - c * 20) // 10 + 1):
        t = animals - c - x
        if money == x * 10 + c * 20 + t * 5:
            print(c, x, t)