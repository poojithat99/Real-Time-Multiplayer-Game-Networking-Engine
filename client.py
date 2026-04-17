import socket
import time
import json
import random

from encryption import encrypt_message, decrypt_message
from protocol import create_packet

SERVER_IP = "192.168.137.1"   # Your server laptop IP
PORT = 7050

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

player_id = random.randint(100,999)

position = [0,0]

print("Client started with ID:", player_id)

while True:

    position[0] += random.randint(0,2)
    position[1] += random.randint(0,2)

    packet = create_packet("update", player_id, position)

    encrypted = encrypt_message(packet)

    client.sendto(encrypted, (SERVER_IP, PORT))

    client.settimeout(2)

    try:

        data, _ = client.recvfrom(2048)

        decrypted = decrypt_message(data)

        state = json.loads(decrypted.decode())

        print("Game State:", state["players"])

    except socket.timeout:

        print("Waiting for server response...")

    time.sleep(1)