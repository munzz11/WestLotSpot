import socket
import json
import threading
from datetime import datetime
import time as ti

BUFSIZ = 2048


def send_data(image_url,car_count, time):
    image_file = open(image_url,'rb')
    image_data = image_file.read(BUFSIZ)

    while image_data:
        clientSocket.send(image_data)
        image_data = image_file.read(BUFSIZ)
    image_file.close()
    data = json.dumps({'car_count': car_count, 'time':time})
    clientSocket.sendall(bytes(data).encode("utf-8")) 
    
#create connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverName = '192.168.1.244'
serverPort = 12345
clientSocket.connect((serverName,serverPort))

send_data('Output.jpg', 6, ti.time())
print('connected')
clientSocket.close()
print('client closed')