def setup_profile(name, vacation_dates):
    global n
    n = name
    global date
    date = vacation_dates
 
 
def print_application_for_leave():
    print('Заявление на отпуск в период', date + '.', n)
 
 
def print_holiday_money_claim(amount):
    print('Прошу выплатить', amount, 'отпускных денег.', n)
 
 
def print_attorney_letter(to_whom):
    print('На время отпуска в период', date, 'моим заместителем назначается', to_whom + '.', n)