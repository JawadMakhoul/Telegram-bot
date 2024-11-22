from flask import Flask


app = Flask(__name__)


@app.route('/sanity')
def sanity():return "Server is running"


if __name__ == '__main__':
    app.run(port=5002)
