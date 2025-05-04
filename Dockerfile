
FROM python:3.11-slim

WORKDIR /app

COPY run.py .

RUN pip install spotipy paho-mqtt

CMD ["python", "run.py"]
