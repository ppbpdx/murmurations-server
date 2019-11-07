from flask_script import Server, Manager
from flask_migrate import Migrate
from app import create_app, db

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

server = Server(host="0.0.0.0", port=5000)

manager.add_command("runserver", server)

@manager.command
def create_database():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
