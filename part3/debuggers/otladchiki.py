# 1st assignment------------------------------------------------------
'''print('Добро пожаловать в интернет-банк!')
print('У нас фантастические процентные ставки!')
print('Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,')
print('для вкладов на сумму до 100 тысяч включительно - 20%,')
print('для более 100 тысяч - 30%!')
print('На какую сумму желаете сделать вклад?')
money = float(input())

if money <= 10000:
    money *= 1.1
elif money <= 100000:
    money *= 1.2
elif money > 100000:
    money *= 1.3
	
print('Вы получаете', money, '₽, поздравляем!')'''

# 2nd assignment------------------------------------------------------
'''num = int(input())
first_num = 0
second_num = 1
fib_num = first_num + second_num
while second_num <= num:
	print(fib_num)
	fib_num = first_num + second_num
	first_num = second_num
	second_num = fib_num'''

# 3rd assignment------------------------------------------------------
'''stone = int(input())

while stone != 0:
	take = int(input())
	stone -= take
	print(stone)'''

# 4th assignment------------------------------------------------------
'''stone = int(input())

while stone != 0:
	take = int(input())
	if take <= 3 and take > 0 and take <= stone:
		stone -= take
		print(stone)
	else:
		print(stone)'''

# 5th assignment------------------------------------------------------
'''stone = int(input())
user = False

while stone != 0:
	if user is False and stone > 3:
		stone -= 1
		print(1, stone)
		if stone <= 3:
			print(stone, end=' ')
			stone -= stone
			print(stone)
			print('ИИ выиграл!')
			user = False
		else:
			user = True
	elif user:
		take = int(input())
		if take <= 3 and take > 0 and take <= stone:
			stone -= take
			print(take, stone)
			user = False
		else:
			print('Некорректный ход:', take)
		if stone == 0:
			print('Вы выиграли!')
			user = True
	elif user is False and stone <= 3:
		print(stone, end=' ')
		stone -= stone
		print(stone)
		print('ИИ выиграл!')'''

'''num = int(input())
cor = 3
while num > 0:
    if num % 4 != 0:
        cor = num % 4
    num -= cor
    print(cor, num)
    if num == 0:
        print("ИИ выиграл!")			# Correct 
    if num <= 0:
        break
    cor = int(input())
    while cor < 1 or cor > 3 or cor > num:
        print("Некорректный ход:", cor)
        cor = int(input())
    num -= cor
    print(cor, num)
    if num == 0:
        print("Вы выиграли!")'''

# 6th assignment------------------------------------------------------
'''n = int(input())
reverse = ''
while n > 0:
	reverse += str(n % 10)
	n //= 10
print(int(reverse))'''

# 7th assignment------------------------------------------------------
'''d = int(input())
month = int(input())
year = int(input())
if month > 2:
	m = month - 2
elif month <= 2:
	m = month + 10
	year -= 1
y = year % 100
c = year // 100
date = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
print(date % 7)
'''

# 8th assignment------------------------------------------------------
'''num = int(input())
count = 0
 
while num > 1:
    count = 1 + num % 2 + count
    num //= 2
print(count)'''

# 9th assignment------------------------------------------------------
'''discount = int(input())

if discount == 0:
	print(50)
elif discount <= 30:
	print(int(discount * 1.5))
elif discount <= 70:
	print(int(discount * 1.1))
else:
	print(discount)'''

# 10th assignment------------------------------------------------------
'''heap1 = int(input())
heap2 = int(input())
while (heap1 != 0) or (heap2 != 0):
	heap = int(input())
	take = int(input())
	if heap == 1:
		heap1 -= take
		print(heap1, heap2)
	elif heap == 2:
		heap2 -= take
		print(heap1, heap2)'''

# 11th assignment------------------------------------------------------
'''heap1 = int(input())
heap2 = int(input())
heap3 = int(input())
while heap1 != 0 or heap2 != 0 or heap3 != 0:
	heap = int(input())
	take = int(input())
	if heap == 1:
		heap1 -= take
		print(heap1, heap2, heap3)
	elif heap == 2:
		heap2 -= take
		print(heap1, heap2, heap3)
	elif heap == 3:
		heap3 -= take
		print(heap1, heap2, heap3)'''

# 12th assignment------------------------------------------------------
'''num = int(input())
first_num = 0
second_num = 1
fib_num = first_num + second_num
count = 1

while second_num <= num:
	fib_num = first_num + second_num
	first_num = second_num
	second_num = fib_num
	count += 1
	if num == fib_num:
		print(count)
		flag = True
		break
	else:
		flag = False
if flag is False:
	print('НЕТ')'''

# 13th assignment------------------------------------------------------
'''money = int(input())
percent = float(input())
year = float(input())

if (float(year) - int(year)) == 0:
	for y in range(1, int(year) + 1):
		money *= 1 + percent / 100
	print(money)
elif (float(year) - int(year)) != 0:
	for y in range(1, int(year) + 1):
		money *= 1 + percent / 100
	money += (money * 0.01) * (float(year) - int(year))
	print(money)'''