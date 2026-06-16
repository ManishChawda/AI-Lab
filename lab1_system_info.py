import os
import json

hostname = os.popen("hostname").read().strip()
kernel = os.popen("uname -r").read().strip()
cpu = os.popen("lscpu | grep 'Model name'").read().strip()
memory = os.popen("free -h | grep Mem").read().strip()
uptime = os.popen("uptime -p").read().strip()

data = {
    "hostname": hostname,
    "kernel": kernel,
    "cpu": cpu,
    "memory": memory,
    "uptime": uptime
}

print(json.dumps(data, indent=4))

