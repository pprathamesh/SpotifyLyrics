
from pprint import pprint
import requests
from musixmatch import musixmatch
from musixmatch.musixmatch import Musixmatch

#paste MusixMatch API key in ''
musixmatch = Musixmatch('')

#paste Spotify API key in ''
SPOTIFY_ACCESS_TOKEN = ''

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        [artists['name'] for artists in artists]
    )
    is_playing = resp_json['is_playing']
    link = resp_json['item']['external_urls']['spotify']

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link,
        "is playing": is_playing
    }

    return current_track_info


def scrape_lyrics(artistname, songname):
    lyrics = musixmatch.matcher_lyrics_get(songname, artistname)

    print(lyrics["message"]["body"]["lyrics"]["lyrics_body"])

    for message in lyrics:
        for body in lyrics[message]:
            if body == "body":
                for lyric in lyrics[message][body]:
                    for lyrBod in lyrics[message][body][lyric]:
                        if lyrBod == "lyrics_body":
                            if (lyrics[message][body][lyric][lyrBod]) == "":
                                print("Lyrics not available due to Copyrights")
                            print(lyrics[message][body][lyric][lyrBod])


def main():
    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    if current_track_info["is playing"]:
        current_lyrics = scrape_lyrics(current_track_info["artists"], current_track_info["name"])
        pprint(current_track_info, indent=4)
        pprint(current_lyrics, indent=4)


if __name__ == '__main__':
    main()
