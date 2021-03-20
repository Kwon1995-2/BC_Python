# str1 = "Python"
# str2 = 'language'
# str3 = """
# multi-line
# string
# example
# """
# print(str3)

# word = 'Python'
# print(word[0:],word[:0], word[20:])
# # word[0] = 'j' -> error

# outStr = ""
# count, i = 0, 0
# inStr = input("Type string : ")
# count = len(inStr)

# for i in range(0, count):
#   outStr = inStr[i] + outStr
# print(outStr)

# for i in range(0, count):
#   outStr += inStr[count-(i+1)]
# print("Reserved string : %s"%outStr)

# print('123'.isdigit())
# print('abvABC'.isalpha())
# print('Ab122'.isalnum())
# print('AB'.isupper())
# print('ab'.islower())
# print(' '.isspace())
###############################
# str = 'Python programming is easy!'
# print(str.upper())
# print(str.lower())
# print(str.swapcase())
# print(str.title())
# print(str.count('i'))
# print(str.find('on'))
# print(str.rfind('sy'))
# print(str.index('on'))
###############################
# str = ' hello '
# print(str)
# print(str.strip())
# print(str.rstrip())
# print(str.lstrip())
###############################
# s = 'a b'
# print(s.split())
# str = 'abc'
# print(str.split('b'))
# print("*".join('hello'))
###############################
str = 'abc'
print(str.center(10))
print(str.center(10,'-'))
print('he'.rjust(5))
print('he'.ljust(5))
print('he'.center(5))
print('12'.zfill(5))







