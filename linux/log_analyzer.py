# log_analyzer.py - flag brute-force logins from an auth log.
# Heuristic: an IP with many "Failed password" lines is suspicious.
# This is the defender's view of the attacks you practise in /web.
import re, collections

# Pre-compiled regex: capture the source IP out of an sshd failure line.
# e.g. "... Failed password for root from 10.0.0.5 port 22 ssh2"
# [0-9]+ = a run of digits; [.] = a literal dot (no escaping needed
# inside a character class). group(1) below = whatever the (...) caught.
FAIL = re.compile(r'Failed password.* from ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)')


def analyze(path="auth.log", threshold=5):
    counts = collections.Counter()       # ip -> failure count
    for line in open(path):
        m = FAIL.search(line)            # None if the line is not a failure
        if m:
            counts[m.group(1)] += 1      # group(1) == the captured IP
    for ip, n in counts.items():         # report the noisy IPs
        if n >= threshold:
            print(f"{ip}: {n} failed logins -> suspicious")


if __name__ == "__main__":
    analyze()
    # Note: a raw count is naive - 100 fails spread over a month is not
    # an attack. TODO: add a TIME WINDOW (N fails within M minutes) by
    # parsing the timestamp; add geo-lookup; emit CSV. That upgrade is
    # the part actually worth talking about in an interview.
