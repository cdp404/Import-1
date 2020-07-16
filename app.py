import func_module

# func_module.module_show()
nowdate = func_module.date_now()
now_year = nowdate.year
now_month = nowdate.month
now_day = nowdate.day
today = '\n{}년 {}월 {}일 입니다.'.format(now_year,now_month,now_day)
print(nowdate)
print(today)

xmas=nowdate.replace(month = 12, day = 25)
xmasday = '\n{}년 {}월 {}일 입니다.'.format(xmas.year,xmas.month,xmas.day)
print(xmasday)