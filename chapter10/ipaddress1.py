import binascii
import ipaddress

ADDRESSES=[
    '192.168.0.5', 
    '164.125.121.191',
    #'2001:0:9d38:6abd:480:flf:3f57:fffb',
]

for ipaddr in ADDRESSES :
    addr = ipaddress.ip_address(ipaddr) #.ip_address(ipaddr)
    print(f'IP address:{addr!r}') 
    print('IP version:',addr.version)
    print("Packed addr:",binascii.hexlify(addr.packed))
    print('Integer addr:', int(addr))
    print('Is private?:',addr.is_private)
    print()
    #파일이름과 예약어 이름 같으면 오류