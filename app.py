from flask import Flask
from flask_cors import CORS

from controller.concept import concept
from controller.inquiry import inquiry
from controller.person import person

app = Flask(__name__)

app.register_blueprint(person, url_prefix='/person')
app.register_blueprint(concept, url_prefix='/concept')
app.register_blueprint(inquiry, url_prefix='/inquiry')
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
