#added functionality to re-send a packet if we do not receive a response in 1 second

import datetime
from socket import *


# server hostname or IP address: 127.0.0.1 or localhost
# needs to match server file
serverName = "127.0.0.1"


# port num > 1023
# needs to match server file
serverPort = 12000


print ("Starting client.")

# sequence number for the packet
sequenceNum = 1

# attempt number (separate from sequence number due to timeouts)
attemptNum = 1

# Boolean to control if we create a new socket and record a new sendTime
# (we do not need a new socket or sendTime if we are re-trying a failed packet)
firstTry = True

while sequenceNum < 11:

    # make a new socket only if we are NOT retrying a failed send
    if firstTry:

        # create the UDP socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        # set the socket to timeout after 1 second
        clientSocket.settimeout(1)

        # capture the approx. time the message was sent
        sendTime = datetime.datetime.now()

        # store the message
        message = "This sequence number is " + str(sequenceNum) + " and it was sent at " + str(sendTime)

    try:

        # show how many attempted sends we have tried
        print ("Attempt number " + str(attemptNum))

        # sends message
        clientSocket.sendto(message, (serverName, serverPort))

        print ("The message to be sent: " + message)

        # Ask for response from server
        modifiedSentence = clientSocket.recv(1024)

        # capture the time the approx. message was received
        receivedTime = datetime.datetime.now()

        print ("Response from server: " + modifiedSentence)

        # calculate RTT in seconds
        RTT = (receivedTime - sendTime).total_seconds()

        print ("The total RTT for this packet was " + str(RTT) + " seconds.\n")

        # close this socket
        clientSocket.close()

        sequenceNum += 1

        # needed in case we are re-sending a packet and firstTry is currently False
        firstTry = True

    except timeout:

        # sanity check to confirm that we are only timing out after 1 second
        timeoutTime = datetime.datetime.now()
        timeoutCheck = round((timeoutTime - sendTime).total_seconds(),1)

        # tell the user that we have timed out
        print ("We have waited " + str(timeoutCheck) + " seconds for the response.\nRequest timed out.\nTrying again.\n")

        # change the message to show that we are retrying to send this packet
        message = "Retry of sequence number " + str(sequenceNum) + " which was originally sent at " + str(sendTime)

        # change boolean to show that we are now re-trying a message and so we do not need to create a new Socket

        firstTry = False

    finally:

        # increment attemptNum after every single try
        attemptNum += 1
