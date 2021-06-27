# DDoS Python Script
A distributed denial-of-service (DDoS) is an attempt to disrupt the normal traffic of a targeted server, service or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic.

WARNING: DO NOT run a DDoS attack on any ip addresses/domain/companies without authorized permission. You could face serious consequences.

### Edit This

```
target = "192.168.1.1"                              
port = 80                                           
conn = 10000
```

- `Target`, the ip address you want to target. It can also be website domain names. 
- `port`, the port you want to attack. For e.g, port 80 is HTTP while port 22 is SSH.
- `conn`, the number of times the script will open connection then disconnect with the server.

### Optimizing the code

```
print("|[DDoS Attack Engaged] |") 
```

Comment out the above line of code if necessary since it slows down the script quite a lot. 

### Using Threading (optional)

```
import threading

for i in range(500):                             
    thread = threading.thread(target=dos)
    thread.start()
```
To make use of Python threading, simply uncomment the above part of the code and run the script.
