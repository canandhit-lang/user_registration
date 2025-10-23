import psycopg2
from flask import Flask,render_template, request,redirect,url_for
app=Flask(__name__)

def get_db_conn():
    conn=psycopg2.connect(
        host="localhost",
        database="user_registration",
        user="postgres",
        password="3489",
        port="5432"
    )
    return conn
@app.route('/')
def home():
    return render_template('register.html')
    
@app.route('/register',methods=['GET','POST'])

def register():
    if request.method == 'POST':
        name=request.form['name']
        sure_name=request.form['sure_name']
        dob=request.form['dob']
        mobile=request.form['mobile']
        email=request.form['email']
        address=request.form['address']

        conn=get_db_conn()
        cur=conn.cursor()
        cur.execute(""" INSERT INTO users(name,sure_name,dob,mobile,email,address) VALUES(%s,%s,%s,%s,%s,%s)""",(name,sure_name,dob,mobile,email,address))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('welcome',registered_name=name))
    
    return redirect(url_for('register'))
@app.route('/welcome/<registered_name>')
def welcome(registered_name):
    return render_template('welcome.html',registered_name=registered_name)
@app.route('/home')
def back_home():
    return redirect(url_for('home'))

if __name__ =='__main__':
    app.run(debug=True)

