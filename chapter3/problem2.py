'''사용자로부터 cm단위의 길이를 입력받는다.
입력값이 음수이면, "잘못입력하였습니다. 메시지 출력
양수이면, 길이를 인치로 변환(1인치 = 2.54cm)'''

cm = int(input("Enter the cm : "))
if cm <0:
    print("잘못입력하였습니다.")
else :
    print(str(cm*2.54)+"cm")