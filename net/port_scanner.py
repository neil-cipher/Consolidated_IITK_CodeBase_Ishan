"""
port_scanner.py - a tiny TCP "connect" scanner (localhost only).

a port is like a numbered door on a machine; a service listening behind a door
(22 = SSH, 80 = HTTP, 443 = HTTPS) makes that port "open". this script tries
to start a normal TCP handshake with each port in turn - if the handshake
completes, something is listening, so the port is open.

ETHICS / LEGAL (matters): only ever point this at 127.0.0.1 or boxes i own.
port-scanning random machines on the internet is hostile traffic and in India
can fall under the IT Act. defenders scan themselves to find doors they forgot
were left open - thats the only thing im doing here.

how "connect" scanning works: socket.connect_ex() returns 0 if the TCP
handshake succeeded (open), or an error number if it was refused / timed out.
its the politest, most basic scan type - it fully connects, no raw-packet
trickery.
"""
import socket


def scan(host="127.0.0.1", ports=range(1, 1025)):
    """Print every open TCP port on `host` within `ports`.

    Args:
        host:  target, defaults to localhost. keep it to machines you own.
        ports: range/iterable of port numbers (default 1-1024, the
               "well-known" range where the common services live).
    Example:
        >>> scan("127.0.0.1", [22, 80, 443])
        open: 80
    """
    for p in ports:
        s = socket.socket()
        s.settimeout(0.3)                  # without this, closed/filtered
                                           # ports make us hang for ages
        if s.connect_ex((host, p)) == 0:   # 0 == handshake done == OPEN
            print("open:", p)
        s.close()


if __name__ == "__main__":
    scan()
    # sequential -> slow, because the 0.3s timeout dominates on every closed
    # port (1024 ports * up to 0.3s each). the obvious upgrades:
    # todo: threadpool to scan ~50 ports at once, label common ports
    #       (22 ssh / 80 http / 443 https), and an argparse CLI for host+range.
