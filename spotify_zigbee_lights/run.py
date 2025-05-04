import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def main():
    print("Starting Spotify Zigbee Lights add-on...")

    client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        print("Spotify credentials not provided. Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")
        return

    try:
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        print("Connected to Spotify API.")
    except Exception as e:
        print(f"Failed to authenticate with Spotify: {e}")
        return

    while True:
        try:
            playback = sp.current_playback()
            if playback and playback['is_playing']:
                track = playback['item']['name']
                artist = playback['item']['artists'][0]['name']
                print(f"Now playing: {track} by {artist}")
            else:
                print("No active playback.")
        except Exception as e:
            print(f"Error fetching playback info: {e}")

        time.sleep(10)

if __name__ == "__main__":
    main()
