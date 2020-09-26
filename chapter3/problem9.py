""" 정수를 입력받아 그 수의 약수를 모두 출력
m % n = 0 이면 n은 m의 약수이다. 
12의 약수는 1, 2, 3, 4, 6, 12"""

m = int(input("Input the integer : "))
divisor = ''
for n in range(1, m+1):
    if m%n == 0:
         divisor = divisor + str(n)
         if not m == n:
             divisor += ", "
print(divisor)
    