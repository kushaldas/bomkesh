## Installation (for development purpose on a real vpn)

We use [algo](https://github.com/trailofbits/algo) vpn as the base.
Install algo on your favorite server. Remember to use wireguard and
with all default settings.


## Adding a initial iptables rule

Add the following rule on the server. This assumers you did not make
changes in the iptables and IP range of the default algo installation.

```bash
# iptables -I INPUT -s 10.19.49.2 -d 10.19.49.1  -j ACCEPT
```

Next, run **bomkesh** tool in one terminal (use tmux), **ajit** in a second terminal, and the python
web app in another.


```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```
Proper installation instructions are coming in future. 


## License GPLv3+
