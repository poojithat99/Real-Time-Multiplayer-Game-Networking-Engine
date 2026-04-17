import json
import time

def create_packet(packet_type, player_id, position):

    packet = {
        "type": packet_type,
        "player_id": player_id,
        "position": position,
        "timestamp": time.time()
    }

    return json.dumps(packet).encode()


def parse_packet(packet_bytes):

    return json.loads(packet_bytes.decode())