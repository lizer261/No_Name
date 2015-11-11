from flask import Flask, render_template, request, url_for, redirect
import database

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("idea.html")


@app.route('/write', methods=['GET', 'POST'])
def write():
    database.add_theme(request.form['theme'])
    return redirect("/")


@app.route('/my/<theme>', methods=['GET'])
def ret_theme(theme):
    return render_template('theme.html', notes=database.get_note_by_theme(theme))


@app.route('/my/<theme>', methods=['POST'])
def add_to_theme(theme):
    try:
        database.add_note(request.form['note'], theme, request.form['id'])
        return render_template('theme.html', notes=database.get_note_by_theme(theme))
    except KeyError:
        database.add_note(request.form['note'], theme, '-1')
        return render_template('theme.html', notes=database.get_note_by_theme(theme))
#
@app.route('/get_tree', methods=['GET','POST'])
def tree_give():
    return render_template('main.html', notes=database.get_note_by_theme('Карточки'))

@app.route('/static/<path:path>')
def static_proxy(path):
  return app.send_static_file('static'+path)

if __name__ == '__main__':
    app.run(port=80, debug=True)

