# def welcome():
#   print("hello, everybody!")
# welcome()
##################################
# def prtStr(str):
#   print("%s"%str)

# str = "Welcome to Python"
# prtStr(str)
##################################
# def squareArea(s):
#   # area = s*s
#   # return area
#   return s*s
# a = squareArea(5)
# b = squareArea(7)
# print("한변의 길이가 %d인 정사각형의 넓이는 %d"%(5,a))
# print("한변의 길이가 %d인 정사각형의 넓이는 %d"%(7,b))
##################################
# def sum(n):
#   nsum = 0
#   for i in range(1,n+1):
#     nsum += i
#   return nsum
# a = sum(50)
# b = sum(1000)
# print(a,b)
##################################
# def func1():
#   v=10
#   print("func1()의 v = %d"%v)
# def func2():
#   global v
#   v = 30
#   #v=20
#   print("func2()의 v = %d"%v)
# v = 20
# func1()
# func2()
##################################
# def prtMesg(message,count=1):
#   print(message*count)
# prtMesg('default')
# prtMesg('Hi!',5)

# def greet(name, msg="Nothing new?"):
#   print("Hi! ",name+', '+msg)
# greet("Abe")
# greet("Bob","Good Morning!")
##################################
# def func(a,b=2,c=3):
#   print('a=',a,'b=',b,'c=',c)
#   return a+b+c
# print(func(4,5))
# print(func(5, c=7))
# print(func(c=10,a=27))
##################################
# def total(*numbers):
#   sum = 0
#   for n in numbers:
#     sum += n
#   return sum
# print(total(1,2,3))
# print(total(1,2,3,4,5))
##################################
# def dicPresident(**keywords):
#   for i in keywords.keys():
#     print("%s : %d-th president"%(i, keywords[i]))

# dicPresident(Kennedy=35, Obama=44, Trump=45)
##################################
# def f(arg):
#   pass
# print(help())
##################################
# sum = lambda x, y : x+y
# print("정수의 합 : ",sum(10,20))
# print("정수의 합 : ",sum(20,20))
# _sum = lambda x,y : (x+y,x*y)
# print(_sum(10,20))
##################################
# def move(n,a,b,c):
#   if n>0:
#     move(n-1,a,c,b)
#     print("Move a disk from %s to %s"%(a,c))
#     move(n-1,b,a,c)
# move(3,'a','b','c')
##################################
# def factorial(n):
#   if n == 0: return 1
#   return n*factorial(n-1)
# print(factorial(5))
##################################
print(abs(-2),round(1.4),round(1.5))
print(all([1,-2,3]),all([1,-2,0]),any([1,-1,-5]),any([0,0,0]))
print(bin(12),oct(9),hex(125))
print(chr(0x41),ord('A'),eval('1+2*3'))
print(enumerate('abc'), list(enumerate('abc')), dict(enumerate('abc')))
print(list(filter(lambda x:len(x)>2,['this','is','a','test'])))
a = map(str.upper,'abc')
print(list(a))
print(max([1,3,9]), min([1,3,9]))
print(repr(b'0011'),repr(11)+"개")
a = zip('abc',(1,2,3))
print(a, list(a))
