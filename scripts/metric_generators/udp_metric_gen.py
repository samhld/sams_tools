import os
import random
import socket
import time
from time import sleep
import gen_config as cfg

addr = '127.0.0.1'
port = 8089
server = (addr,port)

regions = ['us-west-1','us-west2','us-east-1','us-east-2','ap-southeast-2','eu-west-1']
apps = ['checkout','shoes','payment','frontend',]
user_sessions = range(5,2000,45)
num_xactions = range(0,11)

def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.bind((addr,port))

    print("Server running...")
    
    while True:
        line = f"biz_intel,region={random.choice(regions)},app={random.choice(apps)} user_sessions={random.choice(user_sessions)},num_transactions={random.choice(num_xactions)} {time.time_ns()}\n"
        s.connect(server)
        #s.sendto(line.encode('utf-8'), server)
        s.send(line.encode('utf-8'))
        sleep(cfg.settings['interval'])
    s.close() 

if __name__ == '__main__':
    Main()