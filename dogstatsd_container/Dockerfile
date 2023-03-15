FROM python:latest
RUN pip3 install datadog

ADD dogstatsd.py  ./


CMD ["python3", "./dogstatsd.py"]