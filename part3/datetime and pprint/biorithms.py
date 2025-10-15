import datetime
from math import sin, pi, floor


def bio_rhythm(P, T):
    return floor(sin(2.0 * pi * T / P) * 10000) / 100


date = input()
year0, month0, day0 = map(int, date.split('.'))
date0 = datetime.date(day0, month0, year0)

date = input()
year, month, day = map(int, date.split('.'))
date = datetime.date(day, month, year)

t = (date - date0).days

print(bio_rhythm(23, t))
print(bio_rhythm(28, t))
print(bio_rhythm(33, t))