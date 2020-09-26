


m_str = str(input("Input the string:"))
#문자열의 문자수를 출력하라
print(len(m_str))
#문자열을 10번 반복한 문자열을 출력하라
for i in range(0, 10): #range 붙여주기
    print(m_str)
#문자열에서 첫 번째 문자를 출력
print(m_str[0])
#문자열에서 처음 3문자 출력
print(m_str[:3])
#문자열에서 마지막 3문자를 출력
print(m_str[-3:])
#문자열을 거꾸로 출력
print(m_str[::-1])
'''print(m_str[3::-1])'''
#문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다.'출력
if len(m_str) >= 7:
    if not m_str[6] == None:
        print(m_str[6])
    else :
        print("문자가 없습니다.")
else :
    print("Out of string range")

#문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라

#문자를 모두 대문자로 변경하여 출력
print(m_str.upper())
#문자를 모두 소문자로 변경하여 출력
print(m_str.lower())
#문자열에서 'a'를 'e'로 대체하여 출력
if m_str.find('a') != -1:
    m_str.replace('a','e')
    print(m_str)
else :
    print("'a' not exits")


