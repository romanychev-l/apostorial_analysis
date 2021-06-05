from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import analysis
import base64


UPLOAD_FOLDER = '/var/www/apostorial_analysis/dev/uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, resources={r'/*': {'origins': '*'}})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/get_file', methods=['POST'])
def upload_file():
    try:
        print("OKK")
        file = request.files['inputfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            try:
                analysis.get_plt()
            except Exception as e:
                print('e', e)

            with open("images/img.jpg", "rb") as img_file:
                img = base64.b64encode(img_file.read())
                #print(img)
        return jsonify({'base64': img.decode('utf-8')})
    except Exception as e:
        print(e)
        return jsonify({'server': 'error'}), 400


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=7780,
        debug=True,
        threaded=True,
    )
