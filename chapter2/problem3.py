"""원의 반지름을 입력받아 원의 둘레와 원의 면적을 출력하라"""

PI = 3.141592
r = float(input("r of circle : ")) #타입을 맞추자
print("%f %f"%(2*PI*r,PI*r*r))
print(2*PI*r,PI*r**2)
print(2*PI*r,PI*pow(r,2)) #pow는 내장함수