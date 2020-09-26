''' 초를 입력하면 분과 초로 표시하는 프로그램
200초를 입력하면 3분 20초로 표현하라'''

second = int(input("second : "))
minute = second//60
second = second - minute*60
print(str(minute)+'분 '+str(second)+'초')