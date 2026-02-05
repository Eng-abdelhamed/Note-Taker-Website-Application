
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('DB_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DB_NAME')

mysql=MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form['note']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO notes (content) VALUES (%s)", (note,)
        )
        mysql.connection.commit()
        cur.close()
        return redirect('/')

    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT content, created_at FROM notes ORDER BY created_at DESC"
    )
    notes = cur.fetchall()
    cur.close()

    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
