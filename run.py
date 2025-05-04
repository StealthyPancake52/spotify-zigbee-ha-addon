
import time
import json
import os
import paho.mqtt.client as mqtt
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

import logging
logging.basicConfig(level=logging.INFO)

def get_env_config():
    config_path = '/data/options.json'
    with open(config_path, 'r') as f:
        return json.load(f)

def publish_mqtt(mqtt_client, topic, payload):
    mqtt_client.publish(topic, json.dumps(payload))

def main():
    config = get_env_config()
    client_id = config['spotify_client_id']
    client_secret = config['spotify_client_secret']
    mqtt_broker = config['mqtt_broker'].replace("mqtt://", "")
    bulbs = config['bulbs']

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = Spotify(auth_manager=auth_manager)

    mqtt_client = mqtt.Client()
    mqtt_client.connect(mqtt_broker, 1883, 60)

    logging.info("Connected to MQTT and Spotify API")

    while True:
        current = sp.current_playback()
        if not current or not current.get('is_playing'):
            logging.info("Nothing playing")
            time.sleep(5)
            continue

        track_id = current['item']['id']
        analysis = sp.audio_analysis(track_id)
        beats = analysis['beats']

        logging.info(f"Track: {current['item']['name']} - {len(beats)} beats")

        for beat in beats:
            duration = beat['duration']
            for bulb in bulbs:
                payload = {
                    "state": "ON",
                    "color": {"r": 255, "g": 0, "b": 0},
                    "transition": duration
                }
                topic = f"zigbee2mqtt/{bulb}/set"
                publish_mqtt(mqtt_client, topic, payload)
            time.sleep(duration)

if __name__ == "__main__":
    main()
