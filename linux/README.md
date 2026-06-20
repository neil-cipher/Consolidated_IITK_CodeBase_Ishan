# linux/ - brute-force log reader
reads an auth log, flags ips with too many failed logins. run: `python log_analyzer.py` (uses the sample `auth.log`).
todo: real time-windows, ip geolocation, maybe a small chart.
inspired by github.com/gavin-hecke/brute-force-detection (my own code).
