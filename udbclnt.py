import socket
from common import ip_checksum
from operator import xor
import time
serverName = 'localhost'
serverPort = 12000
ack = False
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
 message = raw_input('Input lowercase sentence: ')
 theName = message.encode('utf-8')
 Cs = ip_checksum(theName)
 sendedstring = str(theName) + " " + str(Cs)+" "+str(ack)
 start_time = time.time()
 clientSocket.sendto(sendedstring.encode('UTF-8'),(serverName, serverPort))
 data=""
 data, clientAddress = clientSocket.recvfrom(2048)
 while(data =="ERROR"):
      print("ERROR AND SENDING TO TRY AGAIN  ")
      end_time=time.time()
      if(end_time-start_time > 1):
          clientSocket.sendto(sendedstring.encode('UTF-8'), (serverName, serverPort))
          data, clientAddress = clientSocket.recvfrom(2048)


 ack= xor(ack,True)
 print (data.decode('UTF-8'))
 #clientSocket.close()

