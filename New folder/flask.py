# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:01:17 2023

@author: Home


from flask import Flask
app= Flask(__name__)

@app.route("/")
def index():
    return <h>sf</h>

if __name__=="__main_)":
    app.run(debug=True
    """
    
    
    
    from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confim", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        c = request.form.get('city')
        return render_template('confirm.html',name=n,age=a,city=c)

if __name__ == "__main__":
    app.run(debug=True)









<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register Success</title>
</head>
<body>
<h3>Registration Success</h3>
<table>
     <tr>
         <td>Name</td><td>{{name}}</td>
     </tr>
     <tr>
         <td>Age</td><td>{{age}}</td>
     </tr>
     <tr>
        <td>City</td><td>{{city}}</td>
     </tr>
 </table>
</body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration</title>
</head>
<body>
<form action="/confim" method="post">
    <label>Name</label>
    <input type="text" name="name">
     <label>Age</label>
    <input type="text" name="age">
     <label>City</label>
    <input type="text" name="city">
    <input type="submit" value="Register">
</form>
</body>
</html>






