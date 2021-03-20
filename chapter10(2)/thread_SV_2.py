#_thread를 이용한 TCP 서버 프로그램
import socket, _thread
# def TCP_SV(port):
BUFF = 1024
HOST = '' #'127.0.0.1'
PORT = 2500

#응답 메시지 만드는 함수
def response(key):
    return 'ret:'+key
#클라이언트 연결을 처리할 핸들러
def handler(clientsock, addr): #thread가 얘로 만들어짐 -> 함수 자체가 thread
    #메시지 수신을 위한 루프
    while True:
        #메시지 수신
        data = clientsock.recv(BUFF)
        if not data:
            #print("disconnect by", addr)
            break

        #수신 데이터 화면 출력
        print("data: "+data.decode())
        #c에서 받을 때 c에서 받는 코드가 없기 때문
        #응답 전송
        #clientsock.send(response(data.decode()).encode())
        #print("sent: "+response(data.decode()))

#IPv4, TCP 소켓을 만들어서 변수 sock에 할당
serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#소켓 객체와 포트를 연결
serversock.bind((HOST, PORT))
#클라이언트 연결 대기 모드
serversock.listen(5)
#클라이언트 연결 대기를 위한 루프
while True:
    print('waiting for connection...')
    #클라이언트 연결 요청

    clientsock, addr = serversock.accept()
    print('_connection from ', addr)
    #새로운 쓰레드 만들어서 연결 처리
    _thread.start_new_thread(handler, (clientsock, addr))