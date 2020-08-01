import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import cv2
from decouple import config
from functions.main import getDominantColor, catOrDog, allowed_file


HOST = config('PORT')

UPLOAD_FOLDER = './Uploads/'
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def hello():
    return '''
    	<!doctype html>
    	<h1>This is Index pages</h1>
    	<a href='/cats_vs_dogs'>cats vs dogs</a>
    	'''


@app.route('/cats_vs_dogs', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = cv2.imread(os.path.dirname(os.path.realpath(__file__)) + "/Uploads/" + filename)
            color_result = getDominantColor(image)
            result = catOrDog(image)
            redirect(url_for('upload_file', filename=filename))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '''
			<!doctype html>
			<title>Results</title>
			<h1>Image contains a - ''' + result + '''</h1>
			<h2>Dominant color is - ''' + color_result + '''</h2>
			<form method=post enctype=multipart/form-data>
			  <input type=file name=file>
			  <input type=submit value=Upload>
			</form>
			'''
    return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=submit value=Upload>
	</form>
	'''


if __name__ == "__main__":
    app.run(HOST)