from flask import Flask
from flask import render_template
from flask import request, redirect , url_for
import db


app = Flask(__name__)



@app.route("/")
def home_page():
    return render_template('home.html' )



@app.route("/login", methods=['GET','POST'])
def login_page():
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
         
        connect=db.get_db()
        row = connect.execute(f""" SELECT username, passcode from patient where username = "{username}";""")
        result = row.fetchone()
        
        db.close_db(connect) 
        if result:
            if result[0] == username and result[1] == password:
                
                return redirect(url_for('search'))
                    
            else:
                
                return render_template('login.html')

    return render_template('login.html')


@app.route("/search", methods=['POST','GET'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        # Search
        connect = db.get_db().cursor()
        connect.execute(f'SELECT * FROM Doctors WHERE hospitalName= "{search}";')
            
        result = connect.fetchall()
        db.close_db(connect)
        return render_template('search.html', result=result)
    elif request.method == 'GET':
        connect = db.get_db().cursor()
        connect.execute(f'SELECT * FROM Doctors LIMIT 10;')
        result = connect.fetchall()
        db.close_db(connect)
        return render_template('search.html', result=result)

@app.route("/policy")
def policy_page():
    return render_template('policy_ft.html')

@app.route("/contactUs")
def contactUs_page():
    return render_template('contact_ft.html')

@app.route("/aboutUs")
def aboutUs_page():
    return render_template('about_us.html')

@app.route("/ourteam")
def ourteam_page():
    return render_template('our_team.html')


@app.route("/speciality")
def speciality_page():
    return render_template('speciality_ft.html')

@app.route("/area")
def area_page():
    return render_template('area.html')

@app.route("/doctors", methods=['GET'])
def doctor_page():
    if request.method == 'GET':
        connect = db.get_db().cursor()
        connect.execute(f'SELECT firstname, hospitalName, speciality FROM Doctors;')
        result = connect.fetchall()
        db.close_db(connect)
    return render_template('doctors_ft.html', result=result)
    

@app.route('/signup',methods=['GET','POST'])
def signUp_page():
    if request.method == 'POST' :
        fName = request.form['firstname']
        lName = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        phonemuber = request.form['phonenumber']
        age = request.form['age']
        gender= request.form.get('gender')
        #insert to database 
        connect=db.get_db()
        connect.execute(f"""INSERT INTO patient (firstName,lastName,username,passcode,phone,age,gender) 
                            VALUES('{fName}','{lName}','{username}','{password}','{phonemuber}','{age}'
                            ,'{gender}');""")
        connect.commit()
        db.close_db(connect)
        return redirect(url_for('search'))

    return render_template('signup.html')