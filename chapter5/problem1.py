""" 반지름을 전달하면 원의 면적을 반환하는
cir_area(r) 함수와 원의 둘레를 반환하는 cir_cirm(r)
함수를 작성하라
이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를
소수점 아래 첫 자리까지 구하라"""

def cir_area(r):
    PI = 3.141592
    area = PI*(r**2)
    return area

def cir_cirm(r):
    PI = 3.141592
    cirm = r*2*PI
    return cirm

_r = float(input("Input r : "))
print(round(cir_area(_r),1), round(cir_cirm(_r),1))

    