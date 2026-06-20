# Consolidated_IITK_CodeBase_Ishan

Ishan, Shriram Millennium School Noida. ICSE X (2024) - 95 in Comp Apps + the Academic Excellence award, RoboCup Junior in class X. Came in from competitive programming, like pulling things apart to see how they break.

Putting my stuff in one repo. Few weeks into security so this is beginner-level: small tools I wrote + my lab write-ups. All my own code and it runs.

## inside

- `net/` - tcp port scanner, sockets. own machine only.
- `linux/` - brute-force log reader, run it on the sample `auth.log`.
- `web/` - my write-ups of PortSwigger / Juice Shop / DVWA labs (bug, payload, why, fix). this is the part I'd show first.
- `ctf-writeups/` - picoCTF solves, one per file, flags redacted.
- `evidence/` - X marksheet, excellence award, RoboCup cert.
- `about/` - me in a few lines.

learned each tool from a public tutorial (credited in the file) and rewrote it myself. honest status: a start. tools run, write-ups show how I think through a problem.

## run it

plain python, no deps:

```
cd linux && python log_analyzer.py     # flags the brute-force ip in the sample
cd ../net && python port_scanner.py    # localhost
```

## handles

handle is **neil-cipher**. picoCTF / TryHackMe / Boot.dev being set up under it. PortSwigger & OverTheWire Bandit dont have public profile pages so that work is dated write-ups in `/web` and `/ctf-writeups`.
