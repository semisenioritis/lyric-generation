import requests
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import re
import os
# from search import * # other Python file with functions

######################################################################
########### Main file to run everything #############################
#####################################################################

# Constants
base = "https://api.genius.com"
client_access_token = "%%add your genius api key here%%"

def get_json(path, params=None, headers=None):
    '''Send request and get response in json format.'''

    # Generate request URL
    requrl = '/'.join([base, path])
    token = "Bearer {}".format(client_access_token)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    # Get response object from querying genius api
    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def connect_lyrics(song_id):
    '''Constructs the path of song lyrics.'''
    url = "songs/{}".format(song_id)
    # print("aaaaaaaaaa")
    # print(url)
    data = get_json(url)
    # print("sssssssss")

    # Gets the path of song lyrics
    path = data['response']['song']['path']
    # print(data['response']['song']['path'])
    return path


def retrieve_lyrics(song_id):
    '''Retrieves lyrics from html page.'''
    try:
        path = connect_lyrics(song_id)
        print(path)
        URL = "http://genius.com" + path
        print(URL)
        page = requests.get(URL)
        page=page.text
        # Extract the page's HTML as a string
        html = BeautifulSoup(page, "html.parser")

        # print(html)

        # Scrape the song lyrics from the HTML
        # lyrics = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-5").get_text()
        lyrics = (str(html.find("div", class_="Lyrics__Container-sc-1ynbvzw-5")))
        formatted_lyr=lyrics.replace('<br/>', '\n')
        formatted_lyr = re.sub(r'[\(\[].*?[\)\]]', '', formatted_lyr)

        insoup = BeautifulSoup(formatted_lyr, 'html.parser')

        # Extract only the text
        formatted_lyr = insoup.get_text()
        # print( (formatted_lyr))



        # print(lyrics)
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@")



        # remove identifiers like chorus, verse, etc

        # remove empty lines
        # lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
        return formatted_lyr
    except:
        lyrics='\n'
    return lyrics


def get_song_id(artist_id):
    '''Get all the song id from an artist.'''
    current_page = 1
    next_page = True
    songs = [] # to store final song ids

    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page} # the current page
        data = get_json(path=path, params=params) # get json of songs

        page_songs = data['response']['songs']
        if page_songs:
            # Add all the songs of current page
            songs += page_songs
            # Increment current_page value for next loop
            current_page += 1
            print("Page {} finished scraping".format(current_page))
            # If you don't wanna wait too long to scrape, un-comment this
            if current_page == 85:
                break

        else:
            # If page_songs is empty, quit
            next_page = False

    print("Song id were scraped from {} pages".format(current_page))

    # Get all the song ids, excluding not-primary-artist songs.
    songs = [song["id"] for song in songs]
    print("i found all song ids")
    print(songs)

    return songs



def main():
    # Example searches
    term = 'Sonu Nigam'
    artist_id = 151829


    # Grabs all song id's from artist
    songs_ids = get_song_id(artist_id)


    # Scrape lyrics from the songs
    res="mika_cleaned"
    song_lyrics = [retrieve_lyrics(song_id) for song_id in songs_ids]
    for i in range(len(song_lyrics)):
        with open("artists_cleaned/" + res + ".txt", "a") as f:
            to_append=song_lyrics[i]
            to_append= to_append.encode("ascii", "replace").decode("ascii", "replace")
            to_append = to_append.replace("?", " ")
            f.write(to_append)

    # for lyrics in song_lyrics:
    #     print(lyrics)



if __name__ == "__main__":
    main()