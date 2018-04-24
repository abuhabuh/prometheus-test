import prometheus_client
import flask
import random
import time
import threading

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

application = flask.Flask(__name__)

# Create a metric to track time spent and requests made.
class Metrics:
  summary_base = prometheus_client.Summary(
    'summary_request_seconds', 'Time spent processing request',
    ['route'])
  histogram_base = prometheus_client.Histogram(
    'histogram_request_seconds', 'Time spent processing request',
    ['route', 'foo'])
  context_base = prometheus_client.Histogram(
    'ctx_mgr_hist_seconds', 'Time spent processing request',
    ['route'])


summary = Metrics.summary_base.labels(route='/summary')
histogram = Metrics.histogram_base.labels(route='/histogram', foo='bar')


@application.route('/summary')
@summary.time()
def handle_time_endpoint():
    t = rsleep()
    return '/summary: %f\n' % t


@application.route('/histogram')
@histogram.time()
def handle_time_fn():
    t = rsleep()
    return '/histogram: %f\n' % t


@application.route('/context')
def handle_context():
    """Test context
    """
    t = 0
    with Metrics.context_base.labels('/context').time():
        t = rsleep()
    return '/context: %f\n' % t


@application.route('/metrics')
def handle_prometheus_metrics():
    return flask.Response(
        prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def rsleep():
    t = random.random()
    time.sleep(t)
    return t


if __name__ == '__main__':
    print('run local server')
    application.run('0.0.0.0', 5000)

