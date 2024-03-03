from flask import Flask, render_template, request, redirect, url_for, flash
from dbcheckprint import create_database, fetch_records
import sqlite3
app = Flask(__name__)
app.secret_key = 'sed'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        
        create_database()
        store_data(id, name, address)
        
        flash('Data inserted successfully!')
        
        return redirect(url_for('index'))

@app.route('/show_contents')
def show_contents():
    contents = fetch_records()
    return render_template('show_contents.html', contents=contents)

def store_data(id, name, address):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("INSERT INTO records (id, name, address) VALUES (?, ?, ?)", (id, name, address))

    conn.commit()
    conn.close()
    
@app.route('/delete_all', methods=['POST'])
def delete_all():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("DELETE FROM records")

    conn.commit()
    conn.close()

    flash('All data deleted successfully!')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
