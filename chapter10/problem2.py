import socket

addrinfo = socket.getaddrinfo('www.naver.com', 80)
#addrinfo = socket.getaddrinfo('www.dongyang.ac.kr', 80)
print(addrinfo)