import markovify
import pickle
import pronouncing as p
import argparse
import random
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help="The name of the input text")
input_file = 'raps_all.txt'

LINE_LENGTH = [5, 7]

class RapIndex:
    def __init__(self):
        self.rhymeIndex = dict()
        self.markovIndex = dict()


    def addMarkov(self, key, value):
        if key in self.markovIndex:
            if value in self.markovIndex[key]:
                self.markovIndex[key][value] += 1
            else:
                self.markovIndex[key][value] = 1
        else:
            entry = dict()
            entry[value] = 1
            self.markovIndex[key] = entry
    
    def addRhyme(self, word):
        if len(word) == 1 and word not in 'ia':
            return

        phones = p.phones_for_word(word)
        if len(phones) != 0:
            phones = phones[0].split(" ")
            i = len(phones) - 1
            stub = ""
            while i >= 0:
                if any(char.isdigit() for char in phones[i]):
                    if (stub+phones[i]) in self.rhymeIndex:
                        self.rhymeIndex[stub+phones[i]].add(word)
                    else:
                        self.rhymeIndex[stub+phones[i]] = set([word])
                    break
                stub += phones[i]
                i -= 1

    def markovNext(self, word, no_stop=False, always_stop=False):
        if word not in self.markovIndex:
            raise RuntimeError

        choices = []
        for key in self.markovIndex[word]:
            for i in range(self.markovIndex[word][key]):
                if no_stop and key == '--':
                    None # don't add
                else:
                    choices.append(key)
        if always_stop and '--' in choices:
            return '--'
        else:
            if len(choices) == 0:
                return '--'
            return random.choice(choices)

    def getRhymingWords(self, num=2):
        vowels = [key for key in self.rhymeIndex]
        while len(vowels) > 0:
            choice = random.choice(vowels)
            if len(self.rhymeIndex[choice]) < num:
                vowels.remove(choice)
            else:
                words = [word for word in self.rhymeIndex[choice]]
                returnList = []
                while len(returnList) < num:
                    wordChoice = random.choice(words)
                    returnList.append(wordChoice)
                    words.remove(wordChoice)
                return returnList
        return None
    
    def getBars(self, numBars=2, exp_length=6):
        endWords = self.getRhymingWords(num=numBars)

        bars = []
        for word in endWords:
            current_line = word
            current_word = word
            num_words = 1
            while current_word != '--':
                if num_words < LINE_LENGTH[0]:
                    current_word = self.markovNext(current_word, no_stop=True)
                elif num_words > LINE_LENGTH[1]:
                    current_word = self.markovNext(current_word, always_stop=True)
                else:
                    current_word = self.markovNext(current_word)
                if current_word != '--':
                    current_line = current_word + " " + current_line
                num_words += 1
            bars.append(current_line) 
        return bars


        
    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, "rb") as f:
            dump = pickle.load(f)
            self.markovIndex = dump.markovIndex
            self.rhymeIndex = dump.rhymeIndex


def getLyrics():
    index = RapIndex()

    #print("Building rap index!")
    with open(input_file, "r") as f:
        for line in f:
            line = line.replace("\s+", " ")
            if line.strip() != "":
                words = line.split(" ")
                i = len(words) - 1
                if i > 0:
                    index.addRhyme(words[i].strip())
                while i > 0:
                    index.addMarkov(words[i].strip(), words[i-1].strip())
                    i -= 1
                index.addMarkov(words[i].strip(), "--")
    #index.save("index.ind")
    lyrics = []
    for i in range(4):
      rhymeScheme = randint(1,8)
      if rhymeScheme == 1: #ABAB
        lyrics.extend(index.getBars(numBars=2))
        lyrics.extend(index.getBars(numBars=2))
        temp = lyrics[2]
        lyrics [2] = lyrics[1]
        lyrics [1] = temp
      elif rhymeScheme == 2: #XAXA
        lyrics.extend(index.getBars(numBars=1))
        lyrics.extend(index.getBars(numBars=2))
        lyrics.extend(index.getBars(numBars=1))
        temp = lyrics[2]
        lyrics[2] = lyrics[3]
        lyrics [3] = temp
      elif rhymeScheme == 3: #AABB
        lyrics.extend(index.getBars(numBars=2))
        lyrics.extend(index.getBars(numBars=2))
      elif rhymeScheme == 4: #AAAA
        lyrics.extend(index.getBars(numBars=4))
      elif rhymeScheme == 5: #AXAA
        lyrics.extend(index.getBars(numBars=3))
        lyrics.extend(index.getBars(numBars=1))
        temp = lyrics[1]
        lyrics[1] = lyrics[3]
        lyrics[3] = temp
      elif rhymeScheme == 6: #AAXA
        lyrics.extend(index.getBars(numBars=3))
        lyrics.extend(index.getBars(numBars=1))
        temp = lyrics[2]
        lyrics[2] = lyrics[3]
        lyrics[3] = temp
      elif rhymeScheme == 7: #ABBA
        lyrics.extend(index.getBars(numBars=2))
        lyrics.extend(index.getBars(numBars=2))
        temp = lyrics[1]
        lyrics[1] = lyrics[3]
        lyrics[3] = temp
      elif rhymeScheme == 8: #AXXA
        lyrics.extend(index.getBars(numBars=2))
        lyrics.extend(index.getBars(numBars=1))
        lyrics.extend(index.getBars(numBars=1))
        temp = lyrics[1]
        lyrics[1] = lyrics[3]
        lyrics[3] = temp
      lyrics.extend("\n")
    for i in range(len(lyrics)):
      if (len(lyrics[i]) > 2):
        lyrics[i] = lyrics[i] + "."
    printLyrics(lyrics)
    return lyrics

def printLyrics(finalLyrics):
  for i in range((len(finalLyrics))):
    print(finalLyrics[i])
    
if __name__ == '__main__':
    printLyrics()
