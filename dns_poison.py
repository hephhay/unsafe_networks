# Import the socket module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to port 53 (DNS)
s.bind(('', 53))

# Loop forever
while True:
    # Receive a DNS query from the client
    data, addr = s.recvfrom(1024)

    # Extract the domain name from the query
    domain = data[12:].split(b'\x00', 1)[0].decode()

    # Check if the domain is example.com
    if domain == 'example.com':
        # Construct a fake DNS response with the IP address of the fake server
        response = data[:2] + b'\x81\x80' + data[4:6] * 2 + b'\x00\x00\x00\x00' + data[12:] + \
            b'\xc0\x0c\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04' + \
            socket.inet_aton('172.18.0.3')
        # Send the fake response to the client
        s.sendto(response, addr)
    else:
        # Ignore other domains
        pass
