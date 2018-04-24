import prometheus_client
import flask
import random
import time
import threading

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

application = flask.Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = prometheus_client.Summary(
    'request_processing_seconds', 'Time spent processing request',
    ['fn', 'route'])
REQUEST_TIME_ENDPOINT = REQUEST_TIME.labels(fn='time_fn', route='/time-endpoint')
REQUEST_TIME_FN = REQUEST_TIME.labels(fn='time_fn', route='/time-fn')


@application.route('/metrics')
def handle_prometheus_metrics():
    return flask.Response(
        prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@application.route('/time-endpoint')
@REQUEST_TIME_ENDPOINT.time()
def handle_time_endpoint():
    print('handle time endpoint - thread %s\n' % threading.get_ident())
    t = random.random()
    time.sleep(t)
    return 'time-endpoint: %d' % t


@application.route('/time-fn')
@REQUEST_TIME_FN.time()
def handle_time_fn():
    print('handle time fn - thread %s\n' % threading.get_ident())
    t = random.random()
    return time_fn()


def time_fn():
    t = random.random()
    time.sleep(t)
    return 'time_fn helper: %d' % t


if __name__ == '__main__':
    print('run local server')
    application.run('0.0.0.0', 5000)

