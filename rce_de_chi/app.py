from flask import Flask, render_template_string, request, redirect, make_response
import jwt
from os import urandom

secret = urandom(16)
app = Flask(__name__)

new_dia_2024 = "MSEC{Thanks_Onrsa_from_DTU}"

def hehe():
    with open("app.py","r") as f:
        file = f.read()
        file = file.replace(new_dia_2024,"MTA{fake_ne_hihi}")
    with open("app.py","w") as f:
        f.write(file)

hehe()

def generate_token(username):
    payload = {'username': username}
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload['username']
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

login_html = """
<form method="post" action="/login">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <br><br>
    <input type="submit" value="Login">
</form>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if all(
            i not in username for 
            i in "req url get sec".split()):
            token = generate_token(username)
            response = make_response(redirect('/'))
            response.set_cookie('jwt', token)
            return response
    return login_html

@app.route('/')
def home():
    token = request.cookies.get('jwt')
    username = verify_token(token)
    if username:
        return render_template_string(f"""Hep py niuuuu diaaaaaa {username} <3""")
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)