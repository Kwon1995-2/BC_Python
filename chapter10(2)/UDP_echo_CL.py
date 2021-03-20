#UDP 클라이언트 프로그램

#소켓 모듈을 포함시킨다.
import socket
# 한번에 읽어들일 버퍼 사이즈 지정
BUFFSIZE = 1024
# 서버 주소 입력
svrIP = input(("Server IP(default: 127.0.0.1):")) 
if svrIP == "":
    svrIP = '127.0.0.1'#기본주소

#포트 번호 입력
port = input("port(default: 2500): ")
if port == "":
    port = 2500
else :
    port = int(port)
# IPv4, UDP 소켓을 만들어서 변수 sock에 할당 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    #전송 문자 입력
    msg = input("Sending message:")
    #송신 데이터가 없으면 루프 종료
    if not msg: break

    #데이터 전송
    sock.sendto(msg.encode(), (svrIP, port))
    #서버로부터 받을 데이터가 없다면 대기
    #data, addr = sock.recvfrom(BUFFSIZE)
    #print("Server says",data.decode())

print("bye.")