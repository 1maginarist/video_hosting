from flask import Flask
from flask import send_file
from flask_cors import CORS
import logging
from psycopg2 import connect
import boto3
import yaml
import os
import uuid
from flask import g
from prometheus_flask_exporter import PrometheusMetrics

from helpers.service_helpers import get_settings
from s3_module.s3_model import S3


# initializing app instance and metrics collector
app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['CORS_HEADERS'] = 'Content-Type'
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app)
SETTINGS = get_settings()
s3 = S3()
s3= SETTINGS

'''db_conn = connect(database=f"{SETTINGS['postgres']['DBNAME']}",
                  host=f"{SETTINGS['postgres']['HOST']}",
                  user=f"{SETTINGS['postgres']['USER']}",
                  password=f"{SETTINGS['postgres']['PASS']}",
                  port=f"{SETTINGS['postgres']['PORT']}")
cursor = db_conn.cursor()'''


@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request():
    pass


@app.route('/hello', methods=['GET'])
def count_route():

    return {'body': 'hello Ilya'}


@app.route('/get_video_1', methods=['GET'])
def get_video():
    src_path = 'src/'
    file_path = 'src/test_video_1.mp4'

    if not os.path.isfile(file_path):
        return {'error': 'Video file not found'}, 404

    return send_file(file_path, mimetype='video/mp4')

#--------------------------------------------------------------------------------------------------


@app.route('/reg_user', methods=['POST'])
def reg_user():
    pass


@app.route('/reg_company', methods=['POST'])
def reg_company():
    pass


@app.route('/reg_sub_company_user', methods=['POST'])
def reg_sub_company_user():
    pass


@app.route('/auth', methods=['POST'])
def auth():
    pass


@app.route('/show_preview_courses', methods=['GET'])
def show_preview_courses():
    pass


@app.route('/show_preview_companies', methods=['GET'])
def show_preview_companies():
    pass


@app.route('/user_courses', methods=['GET'])
def user_courses():
    pass


@app.route('/play_video', methods=['POST', 'GET'])
def play_video():
    pass


@app.route('/upload_video', methods=['POST'])
def upload_video():
    pass


@app.route('/edit_video', methods=['POST'])
def edit_video():
    pass


@app.route('/delete_video', methods=['POST'])
def delete_video():
    pass


@app.route('/make_course', methods=['POST'])
def make_course():
    pass


@app.route('/edit_course', methods=['POST'])
def edit_course():
    pass


@app.route('/delete_course', methods=['POST'])
def delete_course():
    pass


@app.route('/view_course', methods=['GET'])
def view_course():
    pass


@app.route('/make_module', methods=['POST'])
def make_module():
    pass


@app.route('/delete_module', methods=['POST'])
def delete_module():
    pass


@app.route('/edit_module', methods=['POST'])
def edit_module():
    pass


@app.route('/view_module', methods=['GET'])
def view_module():
    pass


@app.route('/search_course', methods=['GET'])
def search_course():
    pass


@app.route('/search_video', methods=['GET'])
def search_video():
    pass


@app.route('/search_company', methods=['GET'])
def search_company():
    pass


@app.route('/show_company_page', methods=['GET'])
def show_company_page():
    pass


@app.route('/show_user_page', methods=['GET'])
def show_user_page():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
