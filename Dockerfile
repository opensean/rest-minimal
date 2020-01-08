## Sean Landry
FROM python:3.8.0-alpine3.10

ADD . /opt/rest_minimal

WORKDIR /opt/rest_minimal

RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/opt

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
