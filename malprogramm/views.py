from flask import render_template, request, redirect, send_from_directory
from flask_security import login_required
from malprogramm import app
import base64
from malprogramm.models import Image


@app.route('/')
@login_required
def overview():
    return render_template('overview.html')


@app.route('/malen', methods=['POST', 'GET'])
def malen():
    if request.method == 'POST':
        data = request.get_json()
        print(data)

        picture_data = base64.b64decode(data)
        with open('meinbild.png', 'wb') as f:
            f.write(picture_data)
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

@app.route('/gallery')
def gallery():
    all_images = Image.query.all()
    return render_template('gallery.html', images=all_images)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('images', filename)