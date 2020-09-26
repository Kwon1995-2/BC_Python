""" enumerate() 내장함수를 이용하여 사용자가 입력한 문자열에서 'a'문자의 위치를 모두 찾아 출력
'a'가 없으면 'a'가 없습니다는 메시지 출력"""

# m_str = input("Input string : ")
# location = []
# for i, j in enumerate(m_str):
#     # if j != 'a' and i == len(m_str)-1:
#     #     find = False
#     #     print("'a'가 없습니다.")
#     if j == 'a': 
#        location.append(i)
# if len(location) != 0:
#     print(location)
# else :
#     print('a가 없습니다.')

""" 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 정의
딕셔너리를 이용하여 사용자가 1을 입력하면 sum()호출, 2입력하면, sub(), 3->mul(), 4->div()
두 수의 연산을 수행하는 프로그램 작성"""

# def sum(a, b):
#     return a+b
# def sub(a, b):
#     return a-b
# def mul(a, b):
#     return a*b
# def div(a, b):
#     return a/b

# a = int(input("Input number1 : "))
# b = int(input("Input number2 : "))
# m_dict= {'1':sum, '2':sub, '3':mul, '4':div}
# key = input("Choose 1.sum 2.sub 3.mul 4.div : ")
# print(m_dict[key](a,b))

""" 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는  함수 작성
예 문자열 'led=on&motor=off&witch=off'이고 구분 문자가 &, = 일때 {'led':'on','motor':'off', 'witch':'off'}
Hint : dict([['a','b'],['c','d']])-> {a:b,c:d}"""
def section(m_str):
    # 문자열 -> 2차원 리스트로
    l = m_str.split("&")
    array = [[0 for col in range(2)] for row in l]
    #new_str = m_str.split("&")
    for i, j in enumerate(l) : array[i] = j.split("=")
    # _m_str = str.maketrans('=',':')
    # newstr = m_str.translate(_m_str)
    # 리스트를 딕셔너리로 -> dict()
    return dict(array)


print(section(input("Input String : ")))



