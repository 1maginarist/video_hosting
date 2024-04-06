from flask import Flask
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics

# initializing app instance and metrics collector
app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/hello')
def count_route():

    return {'body': 'hello Ilya'}


if __name__ == '__main__':
    serve(app, host='0.0.0.0')
