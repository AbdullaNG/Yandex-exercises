import random


alpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
a = random.choice(alpha)
n, m, k = int(input()), int(input()), int(input())
b = random.randrange(n, m, k)
c = str(random.uniform(1, 9))[:5]
print(f'{a}-{b}-{c}')