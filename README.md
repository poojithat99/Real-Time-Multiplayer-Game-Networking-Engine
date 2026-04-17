# Real-Time Multiplayer Game Networking Engine

## Overview

This project implements a UDP-based networking engine for a real-time multiplayer game where low latency is important.

Multiple clients communicate with a central server using UDP sockets.

## Features

UDP socket communication

Multi-client server

Game state synchronization

Encrypted communication using AES (Fernet)

Latency measurement

## Architecture

Clients send player updates to the server.

Server maintains the global game state and broadcasts updates to all clients.

Client → Server → Broadcast → Clients

## Technologies Used

Python

UDP sockets

Cryptography library

## How to Run

Install dependencies

pip install -r requirements.txt

Run server

python server.py

Run multiple clients

python client.py
python client.py
python client.py

## Example Output

Server

Player 120 latency: 24 ms
<img width="858" height="301" alt="image" src="https://github.com/user-attachments/assets/58b52945-d57e-40b8-bc0d-16c3d7d951e0" />


Client

Game State: {120: [4,2], 350: [3,6]}
<img width="1009" height="434" alt="image" src="https://github.com/user-attachments/assets/aa1241c5-9273-4ac5-86d8-fa170d63d773" />


