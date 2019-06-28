#This program takes a list of Genius URL's and retrieve lyrics data from them and saves the lyrics to a file

import unicodedata
import requests
#Library which makes text extraction / HTML parsing much easier
from bs4 import BeautifulSoup

headers = {'Authorization': 'Bearer 646_Koz3-Vga8nQi5Y6TxxYYcjVAvzkvB3MTZXNrcKf89OhbldSmtVRstyJvrpsB'}

def get_song_lyrics(song_url):
  page = requests.get(song_url)
  html = BeautifulSoup(page.text, 'html.parser')
  [h.extract() for h in html('script')]
  lyrics = html.find('div', class_='lyrics').get_text()

  return lyrics

def print_to_file(lyrics):
  #Change 'w' to 'a' if you want to append lyrics instead
  output_file = open('Lyrics Raw Data.txt', 'w')
  output_file.write('%s'%specific_lyrics)
  output_file.close()

input_file = open('Lyrics Websites.txt')
lyrics_urls = input_file.readlines()
for url in lyrics_urls:
  print(url)
  try:
    current_lyrics = get_song_lyrics(url.strip())
    print_to_file(current_lyrics)
  except AttributeError:
    continue
  except UnicodeEncodeError:
    continue

input_file.close()