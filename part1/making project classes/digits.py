class Digits:
    def __init__(self, num):
        self.num = [int(x) for x in num.split()]

    def make_negative(self):
        for i in range(len(self.num)):
            self.num[i] = -abs(self.num[i])

    def square(self):
        for i in range(len(self.num)):
            self.num[i] = (self.num[i]) ** 2

    def strange_command(self):
        for i in range(len(self.num)):
            if self.num[i] % 5 == 0:
                self.num[i] += 1

    def convert(self):
        for i in range(len(self.num)):
            self.num[i] = str(self.num[i])


digits = Digits(input())
for i in range(int(input())):
    x = input()
    if x == 'square':
        digits.square()
    elif x == 'make_negative':
        digits.make_negative()
    else:
        digits.strange_command()
digits.convert()
print(' '.join(digits.num))