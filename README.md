# Overview

Run a simple python flask server with uwsgi and monitor with Prometheus.
Flask apps are run multi-threaded with single process so client stats for 
Prometheus are set correctly.

References
* http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
* https://github.com/amitsaha/python-prometheus-demo

# Run

* `docker stack deploy -c docker-compose.yml prometheus`
* Attach to a running client container and send requests to the other 
containers to trigger some metrics

# Hacks

* Prometheus yml hardcodes IPs that client Docker containers are assumed to 
boot with
