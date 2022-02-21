from flask import Flask, render_template, request, flash, redirect, jsonify, session
import os
from ml_model import classifier
from werkzeug.utils import secure_filename
from db import db,db_init
from model_db import Feedback


UPLOAD_FOLDER = './static/test_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'static/test_images'


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feedback.db"

db_init(app)


def allowed_file(filename):
    if '.' not in filename:
        return False

    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            session.clear()
            if image.filename == '':
                flash('Please import an image!', category='error')
                return redirect(request.url)

            if not (allowed_file(image.filename)):
                flash('Only PNG/JPG/JPEG formats are allowed!', category='error')
                return redirect(request.url)

            else:
                filename = secure_filename(image.filename)

                savepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(savepath)

                image_classifier = classifier.ImageClassifier(savepath)
                image_classifier.load_model()
                image_classifier.predict()
                results = image_classifier.get_predictions()


                feedback_db = Feedback(img_path=savepath, mimetype=image.mimetype,predict_class=results['Class'])
                db.session.add(feedback_db)
                db.session.commit()
                session['id'] = feedback_db._id

                return render_template('Home.html', results=results, img_path=savepath, feedback=True)

    return render_template('Home.html', results=results, feedback=False)


# Get Feedback
@app.route("/feedback", methods=["POST", "GET"])
def get_feedback():
    feedback = {'status': 'No Data'}
    if request.method == "POST":
        feedback = (request.get_json(silent=True))
        session['feedback'] = feedback
        feedback_db = Feedback.query.filter_by(_id=session['id']).first()
        feedback_db.predict_right = feedback['PREDICT_RIGHT']
        if feedback['PREDICT_RIGHT']=='Yes':
            feedback_db.actual_class = feedback_db.predict_class
        else:
            feedback_db.actual_class = feedback['ACTUAL_CLASS']
        db.session.commit()
    else:
        if 'feedback' in session:
            feedback = session['feedback']
    return jsonify(feedback)


if __name__ == "__main__":

    app.run(debug=True)
