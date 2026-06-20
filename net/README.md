# net/ - tcp port scanner
checks which ports are open via full tcp connect. **localhost / your own machines only.**
run: `python port_scanner.py`
todo: threads for speed, map 22->ssh 80->http 443->https, a --timeout flag.
inspired by github.com/itaynir1/port-scanner (my own code).
