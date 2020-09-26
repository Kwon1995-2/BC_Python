import socket
import time

def timeclient():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #dgram 넣으면 엑세스 안됨
    address = ("164.125.121.172", 5000) #내가 만든 서버를 내가 테스트해보기 때문에 -> localhost
    sock.connect((address)) #서버에 연결 -> server의 accept로 연결
    timestr = sock.recv(1024).decode() #recv -> 서버에서 받을 때까지, 대기
    print("현재 시각:",timestr)

    tt=time.strptime(timestr)
    #print(tt)
    #print('{}{}{} {}:{}:{}'.format(tt.tm_yaer, tt.tm_mon, tt.tm_mday, tt.tm_hour, tt.tm_min, tt.tm_sec))
    print(time.strftime("%Y %b %d (%a) %H:%M:%S",tt))

while(1):
    n = int(input("select [1:get time/0:quit]"))
    if n==0:
        break
    elif n==1:
        timeclient()
    else:
        pass

