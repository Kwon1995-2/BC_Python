''' 두 수의 최대공약수는 두 수를 나누어 떨어지는 가장 큰 수이다.
예를 들어 (16,24)의 최대공약수는 8이다. 
두 수를 입력받아 최대공약수 구해라
큰 수를 적은 수로 나눈 나머지를 구하라
큰 수를 적은 수로 대체하고 작은 수는 나머지로 대체하라
작은 수가 0이 될 때까지 이 과정을 반복하라. 마지막 큰 수가 최대공약수'''

first_num = int(input("Write number1 : "))
second_num = int(input("Write number2 : "))

if first_num >= second_num:
    big_num = first_num
    small_num = second_num
else :
    big_num = second_num 
    small_num = first_num

while small_num != 0:
    temp = big_num % small_num
    big_num = small_num
    small_num = temp
print("두 수의 최대공약수는 ",big_num)
