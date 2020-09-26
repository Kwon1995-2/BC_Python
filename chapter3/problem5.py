#10진수를 입력받아 2진수로 변환하여 출력

decimal = int(input("Input the decimal : "))
result =''
while decimal != 0 :
    #share = decimal % 2
    result = str(decimal % 2) + result
    decimal //= 2
    #print(share,end='')
print(result)
#print('\n')


