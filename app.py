from flask import Flask
from flask import send_file
from flask_cors import CORS
import logging
import boto3
import os
import uuid
from flask import g
from prometheus_flask_exporter import PrometheusMetrics

# initializing app instance and metrics collector
app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['CORS_HEADERS'] = 'Content-Type'
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app)
g.S3_resource = boto3.resource('s3')


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
