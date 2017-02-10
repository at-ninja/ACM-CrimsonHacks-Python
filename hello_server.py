
from flask import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        # Get the name out of the request
        name = request.form['name']
    else:
        # They issued a GET request - no information was provided
        name = None

    # greet the user
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))