import requests 
import json 
import sys
import os
import matplotlib
import sqlite3
import unittest
import csv
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def getAlbumfeatues(artist):
    base_url = f"https://itunes.apple.com/search?term={artist}&entity=song&attribute=allArtistTerm&limit=89"
    response = requests.get(url=base_url)
    json_response = response.json()
    return json_response

#gets artists from the title of a song
def cleanName(name):
    # split artists by "," and "&", then make sure there are no hanging characters or spaces
    names = name.replace('&', ',').split(',')
    for i in range(len(names)):
        names[i] = names[i].split('[')[0].replace(')', '').replace(']', '').strip() 
    return names

#get all artists from a song
def getArtists(song):
    ret = set(cleanName(song['artistName']))
    others = song['trackName']
    if 'feat.' in others:
        for name in cleanName(others.split('feat.')[1]):
            ret.add(name)
    return ret

# generate dictionary with artists and song IDs
def getData(json):
    songs = json['results']
    artists = {}
    songIDs = {}
    for song in songs:
        #GETTING ARTISTS
        a = getArtists(song)
        for artist in a:
            if artist not in artists:
                artists[artist] = 0
            artists[artist] += 1
        
        # GET SONG / SONG ID
        if "feat." in song['trackName'] and 'Drake' not in song['trackName']:
            songIDs[song['trackName']] = song['trackId']
    
    del artists['Drake'] # making sure it's not counting Drake since it's his songs

    return {
        'artists': artists,
        'ids': songIDs
    }



def main():
    json = getAlbumfeatues("drake")
    data = getData(json)
    '''
        data = {
            artsits: {
                name: count, ...
            }
            ids: {
                title: id, ...
            }
        }
    '''
    pprint(data)

if __name__ == '__main__':
    main()