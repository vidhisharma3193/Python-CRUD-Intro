from flask import Flask, redirect, url_for, request
from sqlalchemy import create_engine

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)

@app.route('/charles')
def charles():
    return 'Hi Charles!!'

@app.route('/hello/<name>')
def hello(name):
    return 'Welcome %s' %name

@app.route('/square/<int:number>')
def square(number):
    return 'Square: %d' %(number * number)

@app.route('/users', methods = ['POST', 'GET'])
def users():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('hello', name = user))
    else:
        user = request.args.get('name')
        return redirect(url_for('hello', name = user))

@app.route('/dept')
def dept():
    conn = e.connect()
    #connecting to database
    query = conn.execute('select distinct DEPARTMENT from salaries')
    return {'departments': [i[0] for i in query.cursor.fetchall()]}

@app.route('/department/<string:name>')
def department(name):
    conn = e.connect()
    query = conn.execute("SELECT * FROM salaries WHERE Department='%s'" %name.upper())
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return result





if __name__ == '__main__':
    app.run(debug = True)
