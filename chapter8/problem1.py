#error 처리 -> try - except
data = {'Sun':0, "Mon":1, "Tue":2, "Wed":3, "Thu":4,"Fri":5, "Sat":6}

# while(1) :
#     error_str = input("Input String : ")
#     if error_str in data:
#         print(data[error_str])
#         continue
#     else:
#         print("항목이 없습니다.")
#         break

#error_str = input("Input String : ")
while(1):
    error_str = input("Input String : ")
    try : 
        print(data[error_str])
    except :
        print("항목이 없습니다.")
        break

