#This program takes in a list of Genius URLs for rap artists' homepage. For each homepage, each album link is visited and each
#Link to song lyrics for a song on the album page is saved to an output file

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#headers = {'Authorization': 'Bearer 646_Koz3-Vga8nQi5Y6TxxYYcjVAvzkvB3MTZXNrcKf89OhbldSmtVRstyJvrpsB'}

queue = ['initialize']

#Fill a Queue with a list of all artist websites from an input file
input_file = open('Artist Websites.txt')
artist_urls = input_file.readlines()
for url in artist_urls:
  queue.append(url.strip())

#Print out the url of a lyrics webpage to an output file
def print_urls(out):
  #Change 'w' to 'a' in order to append instead
  output_file = open('Lyrics Websites.txt', 'w')
  output_file.write('%s\n'%out)
  output_file.close()

#For the given album url, find and save all lyrics wepage urls for each song in the album
def album_Songs(URL):
  current = URL
  print('Currently on : ' + current)
  page = requests.get(current)
  html = BeautifulSoup(page.text, 'html.parser')
  for link in html.find_all('a'):
    newLink = link.get('href')
    if newLink == None:
      continue
    if newLink[-6:] == 'lyrics':
      print_urls(newLink)

#For each artist on the queue, visit the url of each of their albums
while len(queue) > 1:
  del queue[0]
  current = queue[0]
  print('Currently on : ' + current)
  page = requests.get(current)
  html = BeautifulSoup(page.text, 'html.parser')
  for link in html.find_all('a'):
    newLink = link.get('href')
    if newLink == None:
      continue
    newLink = newLink.lower().strip()
    newLink = urljoin(current, newLink)
    if '/albums/' in newLink:
      album_Songs(newLink)

input_file.close()