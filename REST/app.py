from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/home')
def home():
    return render_template('base.html', prueba='Prueba')


if __name__ == '__main__':
    app.run()
