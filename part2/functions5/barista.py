def choose_coffee(*coffies):
    not_coffee = False
    for i in coffies:
        if i == 'Эспрессо' and ingredients[0] > 0:
            ingredients[0] -= 1
            return i
        if i == 'Капучино' and ingredients[0] > 0 and ingredients[1] > 2:
            ingredients[0] -= 1
            ingredients[1] -= 3
            return i
        if i == 'Маккиато' and ingredients[0] > 1 and ingredients[1] > 0:
            ingredients[0] -= 2
            ingredients[1] -= 1
            return i
        if i == 'Кофе по-венски' and ingredients[0] > 0 and ingredients[2] > 1:
            ingredients[0] -= 1
            ingredients[2] -= 2
            return i
        if i == 'Латте Маккиато' and ingredients[0] > 0 and ingredients[1] > 1 and ingredients[2] > 0:
            ingredients[0] -= 1
            ingredients[1] -= 2
            ingredients[2] -= 1
            return i
        if i == 'Кон Панна' and ingredients[0] > 0 and ingredients[2] > 0:
            ingredients[0] -= 1
            ingredients[2] -= 1
            return i
        not_coffee = True
    if not_coffee:
        return "К сожалению, не можем предложить Вам напиток"


ingredients = [4, 4, 0]
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))