# port_scanner.py - TCP connect-scan over a port range.
# Idea: a port is "open" if a full TCP handshake completes. We don't
# craft raw packets; we just ask the OS to connect and read the result.
# Scope: localhost / hosts you own. Scanning third parties = hostile traffic.
import socket


def scan(host="127.0.0.1", ports=range(1, 1025)):
    for p in ports:
        s = socket.socket()        # defaults: AF_INET, SOCK_STREAM == TCP
        s.settimeout(0.3)          # don't block forever on filtered/dead ports
        # connect_ex() returns 0 on success (open), an errno otherwise.
        # Use connect_ex, not connect(), so closed ports don't raise.
        if s.connect_ex((host, p)) == 0:
            print(f"open: {p}")
        s.close()                  # free the fd - 1024 open sockets adds up


if __name__ == "__main__":
    scan()
    # Cost: O(ports), sequential, dominated by the timeout on closed
    # ports -> slow. TODO: thread it (concurrent.futures.ThreadPoolExecutor)
    # for ~50x; map well-known ports (22->ssh, 80->http) to names;
    # add an argparse CLI with --host / --ports / --timeout.
