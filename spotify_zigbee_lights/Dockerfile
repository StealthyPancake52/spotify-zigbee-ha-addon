FROM python:3.10-slim

RUN pip install --no-cache-dir requests numpy paho-mqtt spotipy

COPY run.py /run.py

CMD [ "python", "/run.py" ]
