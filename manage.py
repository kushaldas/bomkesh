import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from bomkesh import app, db

migrate = Migrate(app, db)
manager = Manager(app)
server = Server(host="0.0.0.0", port=5000)

manager.add_command("db", MigrateCommand)
manager.add_command("runserver", server)


if __name__ == "__main__":
    manager.run()
