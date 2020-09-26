'''숫자를 문자열로 변환하는 방법 : str(num)
str(12)->'12'가 된다. 
반대로 문자열을 숫자로 변환 : int(string)을 이용
int('12')->12
이를 이용하여 1부터 1000까지의 숫자의 각 자리수 합을 구하라
예를 들어 234->2+3+4=9'''
m_str = ''
for i in range(1,1001):
    sum = 0
    m_str = str(i)
    for j in range(0, len(m_str)):
        sum += int(m_str[j])
    print("%d -> %d"%(i,sum))




