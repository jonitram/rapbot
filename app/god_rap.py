import markovify
import pickle
import pronouncing as p
import argparse
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help="The name of the input text")
input_file = 'Source Text Files/raps_all.txt'

LINE_LENGTH = [5, 7]

class RapIndex:
    def __init__(self):
        self.rhyme_index = dict()
        self.markov_index = dict()


    def add_markov(self, key, value):
        if key in self.markov_index:
            if value in self.markov_index[key]:
                self.markov_index[key][value] += 1
            else:
                self.markov_index[key][value] = 1
        else:
            entry = dict()
            entry[value] = 1
            self.markov_index[key] = entry
    
    def add_rhyme(self, word):
        if len(word) == 1 and word not in 'ia':
            return

        phones = p.phones_for_word(word)
        if len(phones) != 0:
            phones = phones[0].split(" ")
            i = len(phones) - 1
            stub = ""
            while i >= 0:
                if any(char.isdigit() for char in phones[i]):
                    if (stub+phones[i]) in self.rhyme_index:
                        self.rhyme_index[stub+phones[i]].add(word)
                    else:
                        self.rhyme_index[stub+phones[i]] = set([word])
                    break
                stub += phones[i]
                i -= 1

    def markov_next(self, word, no_stop=False, always_stop=False):
        if word not in self.markov_index:
            raise RuntimeError

        choices = []
        for key in self.markov_index[word]:
            for i in range(self.markov_index[word][key]):
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

    def get_rhyming_words(self, num=2):
        vowels = [key for key in self.rhyme_index]
        while len(vowels) > 0:
            choice = random.choice(vowels)
            if len(self.rhyme_index[choice]) < num:
                vowels.remove(choice)
            else:
                words = [word for word in self.rhyme_index[choice]]
                return_list = []
                while len(return_list) < num:
                    word_choice = random.choice(words)
                    return_list.append(word_choice)
                    words.remove(word_choice)
                return return_list
        return None
    
    def get_bars(self, num_bars=2, exp_length=6):
        end_words = self.get_rhyming_words(num=num_bars)

        bars = []
        for word in end_words:
            current_line = word
            current_word = word
            num_words = 1
            while current_word != '--':
                if num_words < LINE_LENGTH[0]:
                    current_word = self.markov_next(current_word, no_stop=True)
                elif num_words > LINE_LENGTH[1]:
                    current_word = self.markov_next(current_word, always_stop=True)
                else:
                    current_word = self.markov_next(current_word)
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
            self.markov_index = dump.markov_index
            self.rhyme_index = dump.rhyme_index


def get_lyrics():
    index = RapIndex()
    index_name = input_file[0:(len(input_file)-4)]+".ind"

    #print("Building rap index!")
    if not os.path.exists(index_name):
    	with open(input_file, "r") as f:
        	for line in f:
            	line = line.replace("\s+", " ")
            	if line.strip() != "":
                	words = line.split(" ")
                	i = len(words) - 1
                	if i > 0:
                    	index.add_rhyme(words[i].strip())
                	while i > 0:
                    	index.add_markov(words[i].strip(), words[i-1].strip())
                    	i -= 1
                	index.add_markov(words[i].strip(), "--")
    	index.save(index_name)
    else:
	index.load(index_name)

    lyrics = []
    for i in range(4):
      rhyme_scheme = randint(1,8)
      if rhyme_scheme == 1: #ABAB
        lyrics.extend(index.get_bars(num_bars=2))
        lyrics.extend(index.get_bars(num_bars=2))
        temp = lyrics[2]
        lyrics [2] = lyrics[1]
        lyrics [1] = temp
      elif rhyme_scheme == 2: #XAXA
        lyrics.extend(index.get_bars(num_bars=1))
        lyrics.extend(index.get_bars(num_bars=2))
        lyrics.extend(index.get_bars(num_bars=1))
        temp = lyrics[2]
        lyrics[2] = lyrics[3]
        lyrics [3] = temp
      elif rhyme_scheme == 3: #AABB
        lyrics.extend(index.get_bars(num_bars=2))
        lyrics.extend(index.get_bars(num_bars=2))
      elif rhyme_scheme == 4: #AAAA
        lyrics.extend(index.get_bars(num_bars=4))
      elif rhyme_scheme == 5: #AXAA
        lyrics.extend(index.get_bars(num_bars=3))
        lyrics.extend(index.get_bars(num_bars=1))
        temp = lyrics[1]
        lyrics[1] = lyrics[3]
        lyrics[3] = temp
      elif rhyme_scheme == 6: #AAXA
        lyrics.extend(index.get_bars(num_bars=3))
        lyrics.extend(index.get_bars(num_bars=1))
        temp = lyrics[2]
        lyrics[2] = lyrics[3]
        lyrics[3] = temp
      elif rhyme_scheme == 7: #ABBA
        lyrics.extend(index.get_bars(num_bars=2))
        lyrics.extend(index.get_bars(num_bars=2))
        temp = lyrics[1]
        lyrics[1] = lyrics[3]
        lyrics[3] = temp
      elif rhyme_scheme == 8: #AXXA
        lyrics.extend(index.get_bars(num_bars=2))
        lyrics.extend(index.get_bars(num_bars=1))
        lyrics.extend(index.get_bars(num_bars=1))
        temp = lyrics[1]
        lyrics[1] = lyrics[3]
        lyrics[3] = temp
    for i in range(len(lyrics)):
        lyrics[i] += "."
    return lyrics

def print_lyrics(final_lyrics):
  for i in range((len(final_lyrics))):
    print(final_lyrics[i])
    
if __name__ == '__main__':
    get_lyrics()
