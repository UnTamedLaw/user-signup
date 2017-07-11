from flask import Flask, request, redirect, render_template 
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


def valid(text):
    if text == " ":
        return False
    else: 
        return True

@app.route("/")
def index():
    return render_template('form_inputs.html')



@app.route('/validate', methods=['POST'])
def validate():
    userName = request.form['userName']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email= request.form['email']



    username_error = ''
    password_error = ''
    email_error = ''
    verification_error = ''
  
    if not valid(userName):
        username_error = 'Not a valid username'
        userName = ''
    else:
        if len(userName) > 20 or len(userName) <= 2:
            username_error ='Username must be between 3 to 20 characters'
            username = ''
    if not valid(password):
        password_error = 'Not a valid password'
    else:
        if len(password) > 20 or len(password) <= 2:
            password_error ='Password must be between 3 to 20 characters'

    if not valid(verify_password):
        verification_error = " Not a valid password"
    else:
        if password != verify_password:
           verification_error="Passwords must match"


    if not valid(email):
        email_error = 'Not a valid email'
        email=''
    else:
        if len(email) > 20 or len(email) <= 2: 
            email_error ='Email must be between 3 to 20 characters'
            email=''
            
        elif email.count("@") != 1:
            email_error='Not a valid email address'
            email=''
        elif email.count(".") != 1: 
            email_error = 'Not a valid email address'
            email=''
        elif email.count(" ") >= 1:
            email_error='Not a valid email address'
            email=''

  
    if not username_error and not password_error and not email_error and not verification_error:
        return render_template('/success.html', Name = userName )
    else: 
        return render_template('form_inputs.html', username_error=username_error, password_error =password_error,
        email_error=email_error, verification_error = verification_error,
        userName = userName,
        email = email)


app.run()