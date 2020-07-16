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





remain_date()

