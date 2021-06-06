from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import analysis
import gist
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
                x_2 = gist.get_plt()
                analysis.get_graph()
            except Exception as e:
                print('e', e)

            with open("images/img.jpg", "rb") as img_file:
                img = base64.b64encode(img_file.read())
                #print(img)
            with open("images/img2.jpg", "rb") as img_file:
                img2 = base64.b64encode(img_file.read())

        return jsonify({'base64_1': img.decode('utf-8'),
                        'base64_2': img2.decode('utf-8'),
                        'xi_2': str(x_2)})
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
