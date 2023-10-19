from flask import Flask, render_template, request, flash
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsdfsdfsdfhdfg4324343'

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="bed8w7",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if records != []:
            return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
        else:
            if username == '' or password == '':
                flash('login and password should not be empty')
            else:
                flash('invalid username or password')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
