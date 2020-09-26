''' 문자'a'가 들어가는 단어를 키보드에서 입력받아 첫 번째 줄에는 'a'
까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력'''

m_str = str(input("Input the string : "))
n = m_str.find('a')
if not  n == -1:
    print(m_str[:n+1])
    print(m_str[n+1:])