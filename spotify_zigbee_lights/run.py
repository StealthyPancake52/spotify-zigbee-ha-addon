import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def main():
    print("🚀 Starting Spotify Zigbee Lights add-on...")

    client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")

<<<<<<< HEAD
    print(f"🧾 SPOTIFY_CLIENT_ID: {client_id if client_id else '[MISSING]'}")
    print(f"🧾 SPOTIFY_CLIENT_SECRET: {'[SET]' if client_secret else '[MISSING]'}")

    if not client_id or not client_secret:
        print("❌ ERROR: Spotify credentials not provided. Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")
=======
    print(f"Loaded Spotify Client ID: {'[HIDDEN]' if client_id else '[MISSING]'}")
    print(f"Loaded Spotify Client Secret: {'[HIDDEN]' if client_secret else '[MISSING]'}")

    if not client_id or not client_secret:
        print("ERROR: Spotify credentials not provided. Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")
>>>>>>> d5bad4dd4bffe0b992bd72248335123e5b51f45d
        return

    try:
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
<<<<<<< HEAD
        print("✅ Successfully connected to Spotify API.")
    except Exception as e:
        print(f"❌ ERROR: Failed to authenticate with Spotify: {e}")
=======
        print("Successfully connected to Spotify API.")
    except Exception as e:
        print(f"ERROR: Failed to authenticate with Spotify: {e}")
>>>>>>> d5bad4dd4bffe0b992bd72248335123e5b51f45d
        return

    while True:
        try:
            playback = sp.current_playback()
            if playback and playback.get('is_playing'):
                track = playback['item']['name']
                artist = playback['item']['artists'][0]['name']
                print(f"🎵 Now playing: {track} by {artist}")
            else:
                print("⏸ No active playback.")
        except Exception as e:
<<<<<<< HEAD
            print(f"❌ ERROR: Failed to fetch playback info: {e}")
=======
            print(f"ERROR: Failed to fetch playback info: {e}")
>>>>>>> d5bad4dd4bffe0b992bd72248335123e5b51f45d

        time.sleep(10)

if __name__ == "__main__":
    main()
