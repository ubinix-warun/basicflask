from flask import Flask
app = Flask(__name__)

@app.route('/places')
def places():
    return 'Build speed test'

@app.route('/')
def hello_world():
    return 'Hello England again!'

if __name__ == '__main__':
    print "RUN WOOP"
