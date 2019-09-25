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

## Setting up dev instance

You will need to get [bomcapture](https://github.com/kushaldas/bomcapture) repository on the server,
on compiling that project, you will have two binaries, **bomcapture**, and **ajit**.

Start a tmux session.

Next, run **bomkesh** tool in one terminal (use tmux), **ajit** in a second terminal, and the python
web app in another.

You will need to install postgresql for creation of databases
Setup an environment variable `DATABASE_URL` and set it to 'postgresql://{user}:{pw}@{url}/{db}'.


```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# create databases
python3 manage.py db init
python3 manage.py db upgrade

python3 app.py
```
The webapp can be seen at <http://10.19.49999.1:5000/dnsqueue>

Proper installation instructions are coming in future. 


## License GPLv3+
