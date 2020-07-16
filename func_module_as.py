import datetime as dt


def module_show():
    module_type = dir(dt)
    print(module_type)


def date_now():
    return dt.datetime.now()
    

def remain_date():
    # print(dt.date.today())
    today = dt.datetime.now()
    xmas = dt.datetime(2020,12,25)
    # print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    return xmas-today



def remain_date_input(nmonth=12,nday=31):
    today = dt.datetime.now()
    xmas = dt.datetime(2020,nmonth,nday)
    nmonth = int(input('원하는 달을 입력하세요 : '))
    nday = int(input('원하는 일을 입력하세요 : '))
    return xmas-today

# nmonth = input('원하는 달을 입력하세요 : ')
# nday = input('원하는 일을 입력하세요 : ')
# print(remain_date_input(int(nmonth),int(nday)))
