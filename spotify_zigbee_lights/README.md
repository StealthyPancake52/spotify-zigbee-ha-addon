
# Spotify Zigbee Lights Add-on

This Home Assistant add-on syncs your Zigbee RGB bulbs with Spotify music, using beat analysis for smooth lighting transitions.

## Features

- Beat-reactive lighting using Spotify's audio analysis API
- MQTT control of Zigbee2MQTT-enabled bulbs
- Configurable list of bulbs per session

## Setup

1. Add this folder to your Home Assistant `/addons` directory.
2. Fill in `spotify_client_id` and `spotify_client_secret` in the add-on config.
3. Make sure your Zigbee bulbs are listed in `bulbs`.
4. Start the add-on and enjoy beat-reactive lights!
