'''
나이=현재년도-태어난 년도 +1
태어난 년도를 입력 받음 input()

from 모듈명 import
'''

from datetime import datetime as dt
current_year=dt.today().year
print("올해는",current_year,"년 입니다.")

year=current_year

print("언제 태어났나요? ")

age=int(input())
age=int(year-age+1)

if 17<=age<20:
    print("고등학생 입니다.")
elif 20<=age<27:
    print("대학생 입니다.")
else:
    print("학생이 아닙니다.")
