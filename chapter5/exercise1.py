def sum(n): #함수 있다는 것만 알고 흘러감
    hab = 0 # hap=0 으로 초기화
    for i in range(1, n+1):
        #hap += i 
        hab = hab + i
    return hab

a = sum(50)
b = sum(1000)
print(a, b)