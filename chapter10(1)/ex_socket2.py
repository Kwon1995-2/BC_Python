import socket

HOSTS = [
    'www.uou.ac.kr',
    'www.dongyang.ac.kr',
    'www.python.org',
    'testname',
    #'https://kwon1995-2.github.io/web1/',
]

for host in HOSTS :
    print(host)
    try:
        name, aliases, address = socket.gethostbyname_ex(host)
        print(' Hostname:',name)
        print(' Aliases:',aliases)
        print(' Address:',address)
    except socket.error as emsg:
        print('ERROR:',emsg)
    print()
