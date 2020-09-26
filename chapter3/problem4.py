"""사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력받는다. 
또 "am" 혹은 "pm"을 입력받고 경과 시간을 나타내는 값을 입력 받는다.
이로부터 최종 시간이 몇 시인지 출력하는 프로그램 작성 """

c_hour = int(input("Enter the hour : "))
daynight = str(input("'am' or 'pm' : "))
plus_hour = int(input("How many hours ahead? "))
new_hour = c_hour + plus_hour

if daynight == 'am' :
    if c_hour + plus_hour >= 12 :
        new_hour -= 12 
        print('pm '+ str(new_hour))
    else :
        print(daynight+str(new_hour))
elif daynight == 'pm' :
    if c_hour + plus_hour >= 12 :
        new_hour -= 12 
        print('am '+ str(new_hour))
    else :
        print(daynight+" "+str(new_hour))
else :
    print("Must Input 'am' or 'pm'! Retry")


#print(daynight+" "+str(c_hour))