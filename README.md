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

### Flask Configurations

You will need to install postgresql for creation of databases.

- Copy `.env.example` to `.env` and modify (or add) configs.
- Need to modify `DATABASE_URL` in `.env` to 'postgresql://{user}:{pw}@{server}/{db}' based on your database configuration

### Install Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Migrate and run Flask server

```bash
# create databases
python3 manage.py db init
python3 manage.py db upgrade

python3 manage.py runserver
```
That should start a server in [http://localhost:5000/dnsqueue](http://localhost:5000/dnsqueue)

If you make changes in the model, run `python3 manage.py db migrate` to create a migration file


The webapp can be seen at <http://10.19.49.1:5000/dnsqueue>

More instructions are coming in future.


## License GPLv3+
