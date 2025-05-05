import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import paho.mqtt.client as mqtt
import os

# Setup Spotify and MQTT
client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
mqtt_broker = "your_mqtt_broker_address"
mqtt_port = 1883
mqtt_topic = "zigbee2mqtt/your_bulb_topic/set"

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)

def control_lights(beat_intensity):
    # Map beat intensity to lighting effects
    color = (255, 0, 0)  # Red (you can adjust based on beat intensity)
    brightness = 100  # Adjust as needed
    payload = {
        "state": "ON",
        "rgb": color,
        "brightness": brightness
    }
    mqtt_client.publish(mqtt_topic, payload)

def main():
    print("🚀 Starting Spotify Zigbee Lights add-on...")

    client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        print("❌ ERROR: Spotify credentials not provided. Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")
        return

    try:
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        print("✅ Successfully connected to Spotify API.")
    except Exception as e:
        print(f"❌ ERROR: Failed to authenticate with Spotify: {e}")
        return

    while True:
        try:
            playback = sp.current_playback()
            if playback and playback.get('is_playing'):
                track_id = playback['item']['id']
                track = playback['item']['name']
                artist = playback['item']['artists'][0]['name']
                print(f"🎵 Now playing: {track} by {artist}")

                # Fetch audio analysis for the current track
                analysis = sp.audio_analysis(track_id)
                beats = analysis['track']['segments']
                
                # Calculate beat intensity (this is a simple placeholder logic)
                beat_intensity = sum([segment['loudness_start'] for segment in beats]) / len(beats)
                
                # Control lights based on beat intensity
                control_lights(beat_intensity)
            else:
                print("⏸ No active playback.")
        except Exception as e:
            print(f"❌ ERROR: Failed to fetch playback info: {e}")

        time.sleep(10)

if __name__ == "__main__":
    main()
