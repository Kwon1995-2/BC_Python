""" 함수를 이용하여 10진수를 2진수로 변환"""
#dec2bin_int(n) : 정수 n을 2진수로 변환

def dec2bin_int(n):
    _n = ''
    while n != 0:
        _n = str(n%2) + _n
        n = n//2
    #_n += str(n)
    return _n

# nn = int(input("Input Integer : "))
# _nn = dec2bin_int(nn)
# print(_nn)

#dec2bin_float(n) : 1보다 작은 소수를 2진수로 변환
def dec2bin_float(n):
    _n = '.'
    count = 0
    while n > float(0) and count != 23: #or count <= 8 : #float은 != or == 표현 좋지 않다. -> or 둘 중 하나 참이면 계속 루프 돈다.
        if n*2 >=1 :
            _n += '1'
            n = n*2 - 1
        else :
            _n += '0'
            n = n*2
        count = count+1 

    return _n #'0.'+_n

# nn = float(input("Input float : "))
# _nn = dec2bin_float(nn)
# print(_nn)

#dec2bin(n):dec2bin_int()와 dec2bin_float()를 이용하여 실수 n을 2진수로 변환
import math
def dec2bin(n):
    real = dec2bin_int(math.trunc(n))
    imag = dec2bin_float(n-int(n))
    return str(real)+str(imag)

nn = float(input("Input float : "))
_nn = dec2bin(nn)
print(_nn)
