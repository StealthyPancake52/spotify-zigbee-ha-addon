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

    # MQTT connection setup
    try:
        mqtt_client.connect(mqtt_broker, mqtt_port)
        print(f"✅ Successfully connected to MQTT broker: {mqtt_broker}")
    except Exception as e:
        print(f"❌ ERROR: Failed to connect to MQTT broker: {e}")
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
