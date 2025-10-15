class Potato:
    def __init__(self, num):
        self.num = num
    
    def __str__(self):
        return f"Potato({self.num})"
    
    def __itruediv__(self, other):
        self.num /= other
        return self
    
    def __truediv__(self, other):
        new_potato = Potato(self.num / other)
        self.num -= new_potato.num
        return new_potato


pt = pt1 = Potato(7)
pt /= 4
print(pt)
pt2 = pt / 3
print(pt, pt1, pt2, sep='\n')