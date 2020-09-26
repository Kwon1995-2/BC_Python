#문자열을 입력받아 다른 문자열과 결합하여 출력
name = input("Name: ")
print("Hello, "+name)

#두 정수를 입력 받아 곱셈 결과 출력
a=int(input('Number1 : ')) #문자열을 입력한 후 정수로 변환
b=int(input('Number2 : '))
print(a*b)

#섭씨온도(C)를 입력 받아 화씨온도(F)로 바꾸어 출력
C = float(input("Type 섭씨온도 : "))
F = C*9/5 + 32 
print('화씨온도는 ',F)