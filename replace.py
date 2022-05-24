#!/usr/bin/env python3
import download
from dotenv import dotenv_values
import sys
import requests
import json

if len(sys.argv) < 3:
    print("not enough arguments\n")
    sys.exit()

config = dotenv_values()

client_id = config['CLIENT_ID']
secret = config['CLIENT_SECRET']
r = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': secret
})
response = json.loads(r.text)
access_token = response['access_token']

client = download.Download(config['API_KEY'], access_token)

client.download_track_manual(sys.argv[1], sys.argv[2])
