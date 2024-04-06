from flask import Flask
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics
import time

# initializing app instance and metrics collector
app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/count/<x>')
def count_route(x):

    return


if __name__ == '__main__':
    app.run(host='localhost', port=8082)
