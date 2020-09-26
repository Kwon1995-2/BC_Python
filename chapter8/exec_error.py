try :
    a = int(input("Type a Number:"))
except Exception as e:
    print("예외가 발생했습니다.",e)
else:
    print(a)