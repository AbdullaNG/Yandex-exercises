'''import random as rd


lt = []
lt1 = []
n = int(input())
txt = input().split(' ! ')
ran = [int(i) for i in input().split()]

for x in range(n):
	while True:
		tp = rd.randrange(ran[1], ran[2], ran[0])
		if tp not in lt:
			lt.append(tp)
			y = tp
			break
	
	while True:
		tp = rd.choice(txt)
		if tp not in lt1:
			lt1.append(tp)
			z = tp
			break
	print(f'Page {rd.randint(5, 300)}: (the importance {y}) incomprehensible {z}.')'''
#-----------------------------------------------------------------------------------------
'''from datetime import datetime, timedelta
import sys


date1 = None
ndays = None
date = {}

for i in sys.stdin:
    i = i.strip()
    if ' ' in i and not i.startswith('20'):
        charm, day = i.rsplit(' ', 1)
        date[int(day)] = charm
    else:
        date1_str, ndays_str = i.split()
        date1 = datetime.strptime(date1_str, "%Y_%m_%d")
        ndays = int(ndays_str)

for i in range(ndays):
    curr = date1 + timedelta(days=i)
    week = curr.weekday()
    if week in date:
        print(f"{curr.strftime('%Y_%m_%d')}; {date[week]}")'''
#-----------------------------------------------------------------------------------------
