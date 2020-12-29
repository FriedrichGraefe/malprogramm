from flask import render_template, request
from flask_security import login_required
from malprogramm import app


@app.route('/')
@login_required
def overview():
    return render_template('overview.html')


@app.route('/malen')
def malen():
    return render_template('malen.html')


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    print(data)
    username = data.get('username')
    print(username)
    return '', 204
