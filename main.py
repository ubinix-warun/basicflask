from flask import Flask
app = Flask(__name__)

@app.route('/places')
def places():
    return 'another route'

@app.route('/')
def hello_world():
    return 'Hello England again!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
