import socket

s = socket.socket()

# Looking for error code to see if port is open
result = s.connect_ex((YOUR_URL_HERE,8090))

if(result == 0): # 0 means it is open/'all clear'
    print('Port is open')
else:
    print('Port is closed')
