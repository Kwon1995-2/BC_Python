"""분(min)을 입력하면 일, 시간, 분으로 출력하는 프로그램
(예 : 1550분은 1일 1시간 50분)"""

minute = int(input("minute : "))
day = minute//(24*60)
minute = minute - day*24*60
hour = minute//60
minute = minute - hour*60
# if day == 0 : 
#     if hour == 0:
#         print(str(minute)+'분')
#     elif hour != 0
#         print(str(hour)+'시간'+str(minute)+'분')
# elif day != 0
#     print(str(day)+'일'+str(hour)+'시간'+str(minute)+'분')
print(str(day)+'일'+str(hour)+'시간'+str(minute)+'분')