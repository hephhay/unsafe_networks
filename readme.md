# Unsafe Network Project

This project demonstrates how to create an unsafe network with a fake server and a client that performs DNS poisoning to redirect requests to the fake server instead of the real one. It also shows how to sniff the packets in the network from the outside.

## Requirements

- Docker
- Docker Compose
- Python 3
- Scapy
- Requests

## Files

- Dockerfile.client: The Dockerfile for building the client image that runs a curl command to get the html document from the server and also runs a dns_poison.py script to spoof DNS responses.
- Dockerfile.server: The Dockerfile for building the server image that serves index.html on port 80 using nginx.
- Dockerfile.fake: The Dockerfile for building the fake image that serves fake.html on port 80 using nginx.
- docker-compose.yml: The docker-compose file for running the three services (client, server, and fake) on a bridge network with aliases.
- dns_poison.py: The Python script that runs on the client container and listens for DNS queries and sends fake responses for example.com with the IP address of the fake server.
- index.html: The html file that is served by the real server on example.com.
- fake.html: The html file that is served by the fake server on fake.com.
- readme.md: This file.

## Usage

To run this project, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory and run `docker-compose up -d` to start the containers in detached mode.
3. Observe the output of the curl command on the client container.
4. Write your own scripts to sniff the packets on the docker network interface and report unencrypted connections and DNS poisoning.
5. To stop and remove the containers, run `docker-compose down`.
