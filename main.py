from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('user_form.html')

@app.route('/', methods=['POST'])
def Valid_Form():
    user_name = request.form['user_name']
    password =request.form['password']
    verify_password =request.form['verify_password']
    email =request.form['email']
    user_name_error = ""
    password_error = ""
    verify_password_error =""
    email_error=""

    if len(user_name) < 3:
        user_name_error ="User name is less then 8 characters"
        user_name=""
    if len(user_name) > 20:
            user_name_error ="User name is more then 20 character"
            user_name=""
    if  " " in user_name == True:
        user_name_error ="User name contains a space"
        user_name=""
            
    if len(password) < 8:
        password_error ="Password is less then 8 characters"
        password=""
    if len(password) > 15:
            password_error ="Password is more then 20 character"
            password=""
    if  " " in password == True:
        password_error ="Password contains a space"  
        password=""
    
    if password !=verify_password:
        verify_password_error =" Your passwords to not match"
        password=""
        verify_password=""
    
    if len(email) == 0:
        not password_error
    else:
        if ("@" in email) and ("."  in email) and (" "  not in email) and (len(email)> 3 and len(email)<20):
            not password_error  
        else:
            email_error="Not a valid email"
            email=""
            


    if (not user_name_error) and (not password_error) and (not verify_password_error) and (not email_error):
        user_name=user_name
        return redirect ('/welcome?user_name={0}'.format(user_name))
    else:
        return render_template('user_form.html', user_name=user_name, 
        password=password, verify_password=verify_password, email=email, 
        user_name_error =user_name_error, password_error=password_error, 
        verify_password_error=verify_password_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    user_name = request.args.get('user_name')
    return render_template('welcome.html', user_name=user_name)


app.run()