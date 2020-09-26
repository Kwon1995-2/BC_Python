def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

def power(x, n):
    prod = 1
    for i in range(1, n+1):
        prod = prod*x
    return prod

if __name__ == '__main__': #이건 무슨 의미일까?? 메인 모듈이 얘냐 아니냐? 
    #// 다른 모듈에서 얘를 import에서 실행하면 얘는 실행하면 안 됨 -> 메인이 아니니까
    # 모듈로 사용될 때는 실행되지 않음
    print(sum(5))
    print(power(2,3))

