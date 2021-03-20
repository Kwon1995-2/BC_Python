import socket
import time
#서버가 대기상태
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ("",5000) #5000번 포트로 대기하겠다.
s.bind(address) #소켓과 주소 결합
s.listen(5) #접속 대기 // 5는 queue의 갯수 -> 5개만 채우고 나머지 denied ex)티켓팅
print("Waiting for request...")
 
while True:
    client, addr = s.accept() #-> client로부터 접속이 되면 실제 대기
    print("Connection requested from", addr)
    client.send(time.ctime(time.time()).encode()) #데이터 보내줌 : 현재 시각 전송
    client.close()


