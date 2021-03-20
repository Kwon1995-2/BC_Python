# import
import thread_SV, UDP_echo_SV

# 프로토콜 선택 옵션
while True:
    choose = int(input("1.TCP  2.UDP : "))
    if choose != 1 and choose != 2:
        print("Select 1 or 2!")
    else:
        break

# 포트 번호 선택
while True:
    port = int(input("port between 1024 and 40000 : "))
    if 1024 <= port <=40000:
        break
    else :
        print("port between 1024 and 40000!!")
    # if choose < 1024 or 40000 < choose:
    #     print("port between 1024 and 40000")
    # else:
    #     break

# 선택된 옵션에 따라 클라이언트 실행
if choose == 1 :
    #TCP 실행
    thread_SV.TCP_SV(port)
else:
    #UDP 실행
    UDP_echo_SV.UDP_SV(port)
