from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'harshit'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'harshit'
app.config['MYSQL_DB'] = 'python'
  
mysql = MySQL(app)
  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        sqlquery = """SELECT * FROM user where email = %s AND password = %s"""
        #sqlquery = ('SELECT * FROM user where email = ''')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sqlquery, (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully !'
            return render_template('user.html')
        else:
          message = 'Please enter correct email / password !'
    return render_template('login.html', message = message)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    session.pop('name', None)
    return redirect(url_for('login'))
  
@app.route('/signup', methods =['GET', 'POST'])
def signup():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address !'
        elif not userName or not password or not email:
            message = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user (name, email, password ) VALUES (%s, %s, %s)', (userName, email, password, ))
            mysql.connection.commit()
            message = 'You have successfully registered !'
            return render_template('login.html', message = message)
    elif request.method == 'GET':
        message = 'Please fill out the form !'
    return render_template('signup.html', message = message)

@app.route('/reset', methods = ['POST', 'GET'])
def reset():
    message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email, ))
        
        account = cursor.fetchone()
        if not account:
            message = 'This email doesnot exists!'
        elif not password or not email:
            message = 'Please fill out the form !'
        else:    
            cursor.execute("""UPDATE user SET password = %s WHERE email= %s""", (email, password, ))
            message = 'Password Updated Successfully !'
            mysql.connection.commit()
            return render_template('login.html', message = message)

    return render_template('reset.html', message = message)

if __name__ == "__main__":
    app.run(debug=True)