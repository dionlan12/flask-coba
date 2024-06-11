from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = '1e1qdw3f'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'coba-flask'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tb_profile (name, age) VALUES (%s, %s)', (name, age))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    elif request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tb_profile')
        profiles = cur.fetchall()
        cur.close()
        return render_template('index.html', profiles=profiles)

if __name__ == '__main__':
    app.run(debug=True)
