from flask import render_template, request, redirect, send_from_directory
from flask_security import login_required
from malprogramm import app, db
import base64
from malprogramm.models import Image


@app.route('/overview')
@login_required
def overview():
    return render_template('overview.html')


@app.route('/')
def startseite():
    return render_template('startseite.html')


@app.route('/malen', methods=['POST', 'GET'])
@login_required
def malen():
    if request.method == 'POST':

        # Daten kommen hier an und werden in data gespeichert.
        data = request.get_json()

        canvasdata = data.get('cdata')
        userid = data.get('userid')
        imagename = data.get('imgname')

        # Unnötiger Anfang vom String wird abgeschnitten.
        canvasdata = canvasdata.split(",", 1)[1]
        print(imagename)
        saveimage = './malprogramm/images/' + imagename + '.png'
        print(canvasdata)

        # Hier wird das Bild in der Image Tabelle gespeichert.
        image = Image(filename=imagename, user_id=userid)
        db.session.add(image)
        db.session.commit()

        # Hier wird das Bild im Ordnerverzeichnis gespeichert
        picture_data = base64.b64decode(canvasdata)
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
