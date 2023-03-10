import questionary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server_in_memory import server as in_memory_server
from server_persistent import server as persistent_server
from server_backup import server as server_backup

def create_app():
	app = Flask(__name__)
	
	answer = questionary.select(
		"Which Server do you want to start?",
		choices=["In memory Server", "Server with persistence", "Integrated Server with backup"]
		).ask()
	
	if answer=="In memory Server":
		app.register_blueprint(in_memory_server)

	if answer=="Server with persistence":
		app.register_blueprint(persistent_server)
	
	if answer=="Integrated Server with backup":
		app.register_blueprint(server_backup)
	
	return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
