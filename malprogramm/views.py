from flask import render_template, request, redirect
from flask_security import login_required
from malprogramm import app


@app.route('/')
@login_required
def overview():
    return render_template('overview.html')


@app.route('/malen')
def malen():
    if request.method == 'POST':
        file.save(f'malprogramm/images/Bild1')
        return redirect('/', code=303)

    else:

     return render_template('malen.html')


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    print(data)
    username = data.get('username')
    print(username)
    return '', 204
