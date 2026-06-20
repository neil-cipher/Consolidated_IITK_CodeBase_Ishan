# linux/ — brute-force log reader
Reads an auth log and flags IPs with too many failed logins in a short window.
Run: `python log_analyzer.py` (point it at a sample `auth.log`).
Make it mine (TODO): real timestamp windows; IP geolocation; a small chart.
Inspired by github.com/gavin-hecke/brute-force-detection (my own code).
