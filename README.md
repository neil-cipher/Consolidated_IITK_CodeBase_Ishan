# Consolidated_IITK_CodeBase_Ishan

I'm Ishan — The Shriram Millennium School, Noida; ICSE Class X (2024), 95 in Computer Applications and the Overall Academic Excellence Award; RoboCup Junior in Class X. I came in through competitive programming and like taking things apart to see how they break.

I'm pulling my work into one repo. I'm a few weeks into security, so this is a beginner's set: small tools I wrote, plus my write-ups of how deliberately-vulnerable apps break. All my own code, and it runs.

## What's inside

- `net/` — a TCP connect-scan port scanner I wrote with sockets (scan your own machine only).
- `linux/` — a brute-force log reader; run it on the sample `auth.log` included.
- `web/` — my write-ups of PortSwigger / Juice Shop / DVWA labs: what I broke, why it worked, and the fix. This is the part I'd point to first.
- `ctf-writeups/` — my picoCTF solves, one file per challenge, flags redacted.
- `evidence/` — my ICSE Class X marksheet, Academic Excellence Award, and RoboCup Junior certificate.
- `about/` — me, in a few lines.

I learned each tool from a public tutorial (credited in the file) and rewrote it in my own words. Honest status: a starting point — the tools run, and the lab write-ups show how I work through a problem.

## Verify it runs

Plain Python, no external deps. From the repo root:

```bash
cd linux && python log_analyzer.py        # flags the brute-force IP in the sample log
cd ../net && python port_scanner.py       # scans localhost ports
```

## Profiles / handles

Account handle **neil-cipher**. picoCTF / TryHackMe / Boot.dev profiles are being set up under this handle as I build a public track record. PortSwigger and OverTheWire Bandit don't expose public profile pages, so that work lives as dated write-ups in `web/` and `ctf-writeups/`.
