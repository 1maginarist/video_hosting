from flask import Flask
from flask import send_file
from flask_cors import CORS
import os
import re
from prometheus_flask_exporter import PrometheusMetrics

# initializing app instance and metrics collector
app = Flask(__name__)
CORS(app)
metrics = PrometheusMetrics(app)


@app.route('/hello')
def count_route():

    return {'body': 'hello Ilya'}


@app.route('/get_video')
def get_video():
    src_path = 'src/'
    file_path = 'src/test_video_1.mp4'

    if not os.path.isfile(file_path):
        return {'error': 'Video file not found'}, 404

    return send_file(file_path, mimetype='video/mp4')


if __name__ == '__main__':
    app.run(host='89.23.112.6', port=8080, threaded=True)
