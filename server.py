import socket
import json
import time
import random

from encryption import encrypt_message, decrypt_message
from protocol import parse_packet

SERVER_IP = "0.0.0.0"
PORT = 7050

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP, PORT))

clients = {}
game_state = {}

packet_count = 0
start_time = time.time()
prev_latency = None

print("UDP Game Server running...")

while True:

    try:
        encrypted_data, addr = server.recvfrom(2048)
        print("Packet received from:", addr)

        data = decrypt_message(encrypted_data)
        packet = parse_packet(data)

        player_id = packet["player_id"]
        position = packet["position"]

        clients[player_id] = addr
        game_state[player_id] = position

        # 🔹 Latency
        latency = time.time() - packet["timestamp"]
        print(f"Player {player_id} latency: {latency*1000:.2f} ms")

        # 🔹 Jitter
        if prev_latency is not None:
            jitter = abs(latency - prev_latency)
            print(f"Jitter: {jitter*1000:.2f} ms")
        prev_latency = latency

        # 🔹 Throughput
        packet_count += 1
        if time.time() - start_time >= 5:
            print(f"Throughput: {packet_count/5:.2f} packets/sec")
            packet_count = 0
            start_time = time.time()

        # 🔹 Packet loss simulation
        if random.random() < 0.2:
            print("Simulated packet loss")
            continue

        # 🔹 Broadcast state
        state_packet = {
            "type": "state_update",
            "players": game_state,
            "timestamp": time.time()
        }

        message = json.dumps(state_packet).encode()
        encrypted = encrypt_message(message)

        for client_addr in clients.values():
            server.sendto(encrypted, client_addr)

    except Exception as e:
        print("Server error:", e)