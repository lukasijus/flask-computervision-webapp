import os
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template
from werkzeug.utils import secure_filename
import cv2
from decouple import config
from functions.main import getDominantColor, catOrDog, allowed_file
from jinja2 import Environment, PackageLoader, select_autoescape
from shutil import copyfile

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)



HOST = config('PORT')

UPLOAD_FOLDER = './Uploads/'
STATIC_FOLDER = './static/'
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


title_papge = env.get_template('title.html')
about_page = env.get_template('about.html')

@app.route('/')
def hello():
    return render_template(title_papge, title='Index page2')

@app.route('/about')
def about():
    return render_template(about_page, title='About page2')

@app.route('/cats_vs_dogs', methods=['GET', 'POST'])
def upload_file():
    cats_vs_dogs_page = env.get_template('cats_vs_dogs.html')
    cats_vs_dogs_results_page = env.get_template('cats_vs_dogs_results.html')
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
            copyfile(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['STATIC_FOLDER'], filename))
            image = cv2.imread(os.path.dirname(os.path.realpath(__file__)) + "/Uploads/" + filename)
            color_result = getDominantColor(image)
            result = catOrDog(image)
            redirect(url_for('upload_file', filename=filename))
            res = render_template(cats_vs_dogs_results_page, filename = os.path.join(app.config['STATIC_FOLDER'], filename),  title_papge = 'Cats vs Dogs Results', result = result, color_result = color_result)
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.remove(os.path.join(app.config['STATIC_FOLDER'], filename))
            return res
    return render_template(cats_vs_dogs_page, title = 'Upload a new file')
