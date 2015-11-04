from flask import Flask, render_template, request, url_for
import database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if database.explode('SELECT * FROM andrew_notes') != None:
        return render_template('main_with_notes')
    else:
        return render_template("main.html")

@app.route('/write', methods=['GET', 'POST'])
def write():
    note=request.form['note']
    database.explode('INSERT INTO andrew_notes (`note`) VALUES ("'+str(note)+'")')
    return '+'

if __name__ == '__main__':
    app.run(port=80)
