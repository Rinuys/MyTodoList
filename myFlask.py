from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/') 
def test():
    return render_template('/test.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)