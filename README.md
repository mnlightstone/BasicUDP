# README

## Assignment
Our assignment was to implement a client program which sends 10 pings to the server via UDP. The server code, which was provided for us, simply converts the message to uppercase and sends it back to the client. The server code was also written in such a way that ~30% of the packets are 'lost,' simulating the fact that UDP does not confirm reliability. The client code must wait 1 second for a response before moving on to the next packet.

I implemented the code such that the client waits for 1 second and then tries again to send the failed packet. It does not move on to the next packet until the current packet is confirmed to be received (marked by the receipt of an uppercased version of the message, an ACK of sorts).
