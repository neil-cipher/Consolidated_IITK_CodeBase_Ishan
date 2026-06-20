# flag brute-force ssh from an auth log.
# heuristic: one ip with too many "Failed password" lines = sus.
# defender side of the web stuff in /web.
import re, collections

# grab the src ip out of an sshd fail line.
# "... Failed password for root from 10.0.0.5 port 22 ssh2"
FAIL = re.compile(r'Failed password.* from ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)')

def analyze(path="auth.log", threshold=5):
    c = collections.Counter()
    for line in open(path):
        m = FAIL.search(line)
        if m:
            c[m.group(1)] += 1      # group(1) = the ip
    for ip, n in c.items():
        if n >= threshold:
            print(f"{ip}: {n} failed logins -> sus")

if __name__ == "__main__":
    analyze()
    # naive: raw count, no time window. 100 fails over a month isnt an attack.
    # todo: N fails within M mins (parse the timestamp), geo lookup, csv out.
    # the time-window upgrade is the bit actually worth talking about.
