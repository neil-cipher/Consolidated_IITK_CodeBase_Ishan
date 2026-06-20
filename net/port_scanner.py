# tcp connect scan. open == handshake completes.
# localhost / own boxes only. scanning randoms = hostile traffic, dont.
import socket

def scan(host="127.0.0.1", ports=range(1, 1025)):
    for p in ports:
        s = socket.socket()
        s.settimeout(0.3)              # else closed/filtered ports hang
        if s.connect_ex((host, p)) == 0:   # 0 = open, errno otherwise
            print("open:", p)
        s.close()

if __name__ == "__main__":
    scan()
    # sequential -> slow (timeout dominates on closed ports).
    # todo: threadpool ~50x, name the common ports (22 ssh / 80 http), argparse cli.
