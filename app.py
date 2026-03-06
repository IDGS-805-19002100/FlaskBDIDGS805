from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
from models import db


from alumnos import alumnos
from maestros import maestros
from cursos.routes import cursos
from inscripciones.routes import inscripciones

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


app.register_blueprint(alumnos, url_prefix='/alumnos')
app.register_blueprint(maestros, url_prefix='/maestros')
app.register_blueprint(cursos, url_prefix='/cursos')
app.register_blueprint(inscripciones, url_prefix='/inscripciones')


@app.route("/", methods=['GET'])
@app.route("/index")
def index():
    
    return render_template("index.html")








@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)