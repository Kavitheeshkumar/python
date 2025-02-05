from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'KADAVULE AJITHEYY'

# main driver function
if __name__ == '__main__':

    app.run()