from flask import Flask, render_template, request, flash, redirect
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="bed8w7",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login():
    if request.form.get("login"):
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        if username != '' and password != '':
            cursor.execute(f"SELECT * FROM service.users WHERE login='{username}'")
            records = list(cursor.fetchall())
            if records == []:
                flash('User not found')
            elif records[0][3] != password:
                flash('Invalid password')
            else:
                return render_template('account.html', full_name=records[0][1], login=records[0][2],
                                       password=records[0][3])
        else:
            flash('Login and password cannot be empty')
    else:
        return redirect("/registration/")
    return render_template('login.html')


@app.route('/registration/', methods=['GET'])
def registration_get():
    return render_template('registration.html')


@app.route('/registration/', methods=['POST'])
def registration_post():
    name = str(request.form.get('name'))
    login = str(request.form.get('login'))
    password = str(request.form.get('password'))
    if len(name) < 1 or len(login) < 6 or len(password) < 6:
        flash('The minimum length of each field is 6 characters')
    else:
        cursor.execute("SELECT login FROM service.users")
        records = list(cursor.fetchall())
        for i in records:
            if i[0] == login:
                flash('This login already exists')
                break
        else:
            cursor.execute("INSERT INTO service.users (full_name, login, password)"
                           "VALUES ('{0}', '{1}', '{2}');".format(name, login, password))
            conn.commit()
            return redirect('/')
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
