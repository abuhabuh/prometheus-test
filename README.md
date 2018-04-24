# Overview

Run a simple python flask server with uwsgi and monitor with Prometheus.
Flask apps are run multi-threaded with single process so client stats for 
Prometheus are set correctly.

References
* https://github.com/prometheus/client_python
* http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
* https://github.com/amitsaha/python-prometheus-demo

# Run

## Compose
* `docker stack deploy -c docker-compose.yml prometheus`
* Attach to a running client container and send requests to the other 
containers to trigger some metrics
* Go to localhost:9090 to see Prometheus console

## Manual
* `docker run -d prom-client`
  * run this N times for N clients
* `docker network inspect bridge` to get ip addresses of clients
* update server/prometheus.yml with IP of clients
* `docker-compose build` to create server image that targets clients
* `docker run -d -p 9090:9090 prom-server`

# Dependencies

* Docker needs to be installed
* Docker swarm needs to be active: `docker swarm init`

# Hacks

* Prometheus yml hardcodes IPs that client Docker containers are assumed to 
boot with

