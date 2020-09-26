"""두 개의 매개변수 n,m을 전달받아 mxn개의 *상자를 출력하는 프로그램"""
# n = int(input("rows : "))
# m = int(input("cloumns : "))
# for i in range(0,n):
#     for j in range(0, m):
#         print("*",end='')
#     print('')

""" 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수"""
# 코드 줄이기
# # 뒤에서 자르기 #enumerate
# def NSum(n):
#     n_list = []
#     exponent = len(str(n)) - 1
#     for i in range(0, exponent+1):
#         n_list.append(n//(10**(exponent-i)))
#         n = n - (n//(10**(exponent-i)))*(10**(exponent-i))
#     return sum(n_list)

# _n = int(input("Input number : "))
# nn = NSum(_n)
# print(nn)

"""두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성, 두 개의 문자열이 같으면 -1을 반환"""

# def location(m1, m2):
#     i = 0
#     while i <= len(m1):
#         if i == len(m1): return -1
#         if m1[i] == m2[i]:
#             i = i+1
#             continue 
#         else :
#             return i

# m_str1 = input("Input the string1 : ")
# m_str2 = input("Input the string2 : ")

# if len(m_str1) != len(m_str2):
#     print("length different")
# else :
#     print(location(m_str1,m_str2))
    

""" 숫자를 전달받아 그 수의 약수를 리스트로 반환"""
# def divisor(n):
#     d_list=[]
#     for i in range(1, n+1):
#         if n % i == 0: 
#             d_list.append(i)
#     return d_list

# number = int(input("Input any Number : "))
# print(divisor(number))


""" 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환"""
# def location(s, c):
#     loc = ''
#     if len(c) > 1 or len(c) <= 0:
#         return "문자 하나를 입력하시오."
#     for i in range(0, len(s)):
#         if s[i] == c :
#             loc = loc + str(i)
#             loc += " "
#     if len(loc) == 0:
#         return "같은 문자열이 없습니다."
#     return loc

# m_str = input("Input String : ")
# m_ch = input("Input Character : ")
# print(location(m_str, m_ch))

""" 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램"""
def Recursive(n):
    if n< 1 : return 0
    return n + Recursive(n-1)

print(Recursive(int(input("Input Number : "))))

    
    
    
    



    
