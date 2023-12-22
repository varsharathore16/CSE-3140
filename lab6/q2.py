from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('q2.html')
    
if __name__ == '__main__':
    app.run(debug=True)