#for문

# for i in[1,2,3] :
#     print("숫자", i)

# for i in(1,2,3):
#     print("숫자", i)

# for i in 'hello':
#     print(i, end='')

# for i in range(1,4,1):
#     print(i)

# sum = 0
# for i in range(1, 101,1):
#     sum += i #sum = sum + i
# print("sum = ", sum)

#//
# x =float(input('Type x : '))
# n = int(input('Type n : '))

# prod = 1
# for i in range(1, n+1):
#     prod = prod*x
# print(prod)
#//

#중첩 반복문
for i in range(1,10,1):
    for j in range(1, 10,1):
        print("%dx%d = %d "%(i,j,i*j),end='')
    print("\n---------------------------------------------------------------------------------")
    
