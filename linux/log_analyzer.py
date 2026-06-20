"""
log_analyzer.py - flag SSH brute-force attempts from an auth log.

when someone tries to guess an SSH password, the server writes a line like
    Jun 20 10:01:00 host sshd[111]: Failed password for root from 203.0.113.9 port 2222 ssh2
for every wrong guess. one IP address racking up loads of these "Failed
password" lines is a classic brute-force signature. this is the defender side
of the web-attack stuff in /web - instead of breaking in, im spotting someone
else trying to.

heuristic (deliberately simple): count the Failed-password lines per source
IP, then shout about any IP at or above a threshold.

the included auth.log is a small hand-made sample so this runs out of the box.
"""
import re, collections

# pull the source IP out of an sshd failure line. the bracketed groups match
# the four numbers of an IPv4 address:
#   "... Failed password for root from 10.0.0.5 port 22 ssh2"
#                                       ^^^^^^^^ <- this is captured
FAIL = re.compile(r'Failed password.* from ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)')


def analyze(path="auth.log", threshold=5):
    """Print each source IP with >= `threshold` failed SSH logins in `path`.

    Args:
        path:      the auth log to read.
        threshold: how many failures before an IP is called suspicious.
    Example:
        >>> analyze("auth.log", threshold=5)
        203.0.113.9: 7 failed logins -> sus
    """
    counts = collections.Counter()
    for line in open(path):
        m = FAIL.search(line)
        if m:
            counts[m.group(1)] += 1      # group(1) = the captured IP
    for ip, n in counts.items():
        if n >= threshold:
            print(f"{ip}: {n} failed logins -> sus")


if __name__ == "__main__":
    analyze()
    # naive bit: its a raw count with no time window, so 100 fails spread over
    # a whole month would falsely look like an attack. the upgrade thats
    # actually worth talking about:
    # todo: count N fails within M minutes (parse the timestamp), then add a
    #       geo lookup on the IP and a csv export.
