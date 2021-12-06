import requests 
import json 
import sys
import os
import matplotlib
import sqlite3
import unittest
import csv
#import numpy as np
import matplotlib.pyplot as plt
from requests.api import request 

def getAlbumfeatues(artist):
    base_url = f"https://itunes.apple.com/search?term={artist}"
    response = requests.get(url=base_url)
    json_response = response.json()
    print(json_response)

def main():
    getAlbumfeatues("drake")

if __name__ == '__main__':
    main()