import datetime


def days_left(date):
	date = datetime.datetime.strptime(date, '%d.%m.%Y')
	today = datetime.datetime.today()
	return (date - today).days