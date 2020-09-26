#예외 처리를 한 TCP 클라이언트 프로그램
#실행할 떄, 서버 주소와 포트를 지정한다.
#지정하지 않으면, '127.0.0.1'과 2500사용

#소켓 모듈을 포함시킨다. - socket()
import socket
#IPv4 TCP 소켓을 만들어서 변수 sock에 할당
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#서버 주소 입력
svrIP = input(("Server IP(default: 127.0.0.1):"))
if svrIP == '':
    svrIP = "127.0.0.1" #기본 주소
#포트 번호 입력
port = input("port(default: 2500)")
if port == "":
    port = 2500 #기본 포트
else :
    port = int(port)

#서버에 접속 - connect()
sock.connect((svrIP, port))
print("Connected to "+svrIP)

#메시지 전송을 위한 루프 - read() & write()
while True:
    #전송문자 입력
    msg = input("Sending message: ")

    #송신 데이터가없으면 루프 종료
    if not msg:
        print("연결을 종료합니다.")
        break

    try :#데이터 전송
        sock.send(msg.encode()) #메시지 전송
    except: #연결이 종료됨
        print("연결이 종료되었습니다.")
        break

    try : #데이터 읽기
        msg = sock.recv(1024)
        if not msg:
            print("연결이 종료되었습니다.")
            break
        print(f"Received message: {msg.decode()}")
    except: #연결이 종료됨
        print("연결이 종료되었습니다.")
        break

sock.close()
    