# SpotifyLyrics
Fetches Lyrics from MusixMatch using Spotify API

This project was created before the Spotify app displayed lyrics. Previously, the project was designed to webscrape genius.com to display the lyrics of the current playing song. After the updates to Genius.com, it makes it illegal to webscrape genius.com. So instead, I have updated this project to use MusixMatch api to fetch lyrics for the current song playing in spotify.

To make sure the project runs,
1) visit https://developer.spotify.com/console/get-user-player/
2) Click get token
3) check the required scope for this endpoint (user-read-playback-state)
4) Click request token
5) Login
6) copy the complete OAuth Token
7) Paste it in '' at line 11 in main.py

Now, to get MusixMatch API key,
1) Visit https://developer.musixmatch.com/signup
2) finish signing up
3) Visit https://developer.musixmatch.com/admin/applications
4) Copy the Key
5) Paste it in '' at line 8 in main.py
