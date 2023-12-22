from flask import Flask, request, make_response
import socket

app = Flask(__name__)

netid = 'vsr19001'
last_name = 'Rathore'

# Function to get the IP address of the VM
def get_vm_ip():
    return socket.gethostbyname(socket.gethostname())

# Route for the root folder
@app.route('/')
def index():
    # Set Cookie Q1B1 with the netid value
    resp = make_response("Welcome to the home page!")
    resp.set_cookie('Q1B1', netid)
    return resp

# Route for folder Q1B2
@app.route('/Q1B2')
def q1b2():
    # Set Cookie Q1B1 (netid) and Q1B2 (last name)
    resp = make_response("Welcome to folder Q1B2!")
    resp.set_cookie('Q1B1', netid)
    resp.set_cookie('Q1B2', last_name)
    return resp

# Route for folder Q1B3
@app.route('/Q1B3')
def q1b3():
    # Set Cookie Q1B1 (netid), Q1B2 (last name), and Q1B3 (VM IP address)
    resp = make_response("Welcome to folder Q1B3!")
    resp.set_cookie('Q1B1', netid)
    resp.set_cookie('Q1B2', last_name)

    # Set Cookie Q1B3 with the VM IP address and mark it as HttpOnly
    resp.set_cookie('Q1B3', get_vm_ip(), httponly=True)

    return resp

if __name__ == '__main__':
    app.run(debug=True)