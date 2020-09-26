#UDP 에코 서버 프로그램

#소켓 모듈을 포함시킨다.
import socket

def UDP_SV(port):
    # listening 포트
    #port = 2500
    #한번에 읽어들일 버퍼 사이즈 지정
    BUFSIZE = 1024
    # IPv4, UDP 소켓을 만들어서 변수 sock에 할당
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #소켓 객체와 포트를 연결, ""를 사용하면 자신의 주소 사용
    sock.bind(("", port))
    print("Waiting for clients...")
    #메시지 수신을 위한 루프
    while True:
        #클라이언트가 보내온 메시지와 클라이언트 주소 읽기
        data, addr = sock.recvfrom(BUFSIZE)
        print("Received message",addr, ":",data.decode())

        #sock.sendto(data,addr)#재전송