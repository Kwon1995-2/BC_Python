#TCP 에코 서버 - 1명의 클라이언트만 서비스한다.

#소켓 모듈을 포함시킨다. - socket()
import socket


#listening port
port = 2500 #1024~40000번 안쪽

#한번에 읽어들일 버퍼 사이즈 지정
BUFSIZE = 1024

#IPv4 TCP 소켓을 만들어서 변수 sock에 할당
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#소켓 객체와 포트를 연결, ""를 사용하면 자신의 주소 사용
sock.bind(("",port)) #bind()

#클라이언트 연결 대기 모드 #listen()
sock.listen(1) #최대 대기 클라이언트 수
print("Waiting for clients...")
#클라이언트 연결 요청 #accept()
c_sock, (r_host, r_port) = sock.accept()
print("connected by",r_host,r_port)
#메시지 수신을 위한 루프 #read & write()
while True:
    #클라이언트가 보내온 메시지 읽기
    data = c_sock.recv(BUFSIZE)
    #클라이언트가 보내온 데이터가 없으면 종료
    if not data: break
    print("Received message: ", data.decode())
    #수신 메시지를 다시 전송
    c_sock.send(data)

print("disconnected by",r_host,r_port)
c_sock.close()

#close - 서버가 닫든 클라이언트가 닫든 한쪽 닫으면 자동 