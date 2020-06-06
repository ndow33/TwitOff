from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

# the name of the db file
DATABASE_URI = "sqlite:///twitoff_dev.db" # using relative filepath

# define a function to create a new flask app based on the home_routes blueprint
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    # takes the home_routes Blueprint object and registers it as an app
    # when this app is created in the code on line 16
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app



if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
