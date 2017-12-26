import socket
from common import ip_checksum
from operator import xor
ack=False
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while 1:
 data, clientAddress = serverSocket.recvfrom(2048)
 message=data.decode("UTF-8")
 data = message.split(' ')
 print(data[0])
 print(data[1])
 print(data[2])
 checksum = ip_checksum(data[0])
 print(checksum)
 if (data[1] != str(checksum) or data[2]!=str(ack)):
	serverSocket.sendto("ERROR", clientAddress)
 else:
	Cname = data[0].upper()
	serverSocket.sendto(Cname.encode("UTF-8"), clientAddress)

 ack= xor(ack,True)