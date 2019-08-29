from pynput.keyboard import Key, Controller
import time
import socket

UDP_PORT = 5005

keyboard = Controller()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT));

print("Aloitetaan kuuntelu")

while True:
    data, addr = sock.recvfrom(1024)
    print("received message:", data)
    if data.decode(encoding="utf-8") == "a":
        keyboard.press('a')

#time.sleep(2)
#keyboard.press('a')
#keyboard.release('a')