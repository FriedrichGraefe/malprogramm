from flask import render_template, request, redirect, send_from_directory
from flask_security import login_required
from malprogramm import app, db
import base64
from malprogramm.models import Image


@app.route('/')
@login_required
def overview():
    return render_template('overview.html')


@app.route('/malen', methods=['POST', 'GET'])
def malen():
    if request.method == 'POST':
        imageid = 0

        data = request.get_json()
        data = data.split(",", 1)[1]
        imagename = data.split("Bildtitel", 1)[1]
        print(imagename)
        saveimage = './malprogramm/images/' + imagename + '.png'
        print(data)
        imageid = imageid + 1

        image = Image(id=imageid, filename=imagename, user_id=1)
        db.session.add(image)
        db.session.commit()

        picture_data = base64.b64decode(data)
        with open(saveimage, 'wb') as f:
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
