import socket

HOSTS = [
    'www.uou.ac.kr',
    'www.dongyang.ac.kr',
    'www.python.org',
    'testname',
    #'https://kwon1995-2.github.io/web1/',
]

for host in HOSTS :
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))
