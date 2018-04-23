FROM python:3.6.5-jessie

WORKDIR /home

COPY src/prom-client.py /home
COPY src/requirements.txt /home
COPY src/uwsgi.ini /home

RUN pip install -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]
