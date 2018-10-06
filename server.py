# UDPPingerServer.py
import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", 12000))
print ("Starting server.")
while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)  #type: #(string, address)

    print ("Message received: " + message)
    message = message.upper()

    print ("Random number is " + str(rand))

    if rand < 4:
        print ("Timing out. \n")
        continue

    print ("Random number is > 4. \nSending response message.\n")
    serverSocket.sendto(message, address)