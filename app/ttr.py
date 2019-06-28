import os
from pydub import AudioSegment
from gtts import gTTS
from lyrics_generator import getLyrics

def textToRap():
	lyr = getLyrics()
	allLyrics = []
	sounds = []
	texttospeech = [] 
	print("", end='')
	for i in range(0,7):
		print("\rVocalizing lyrics part %d of 8..." % (i + 1), end='')
		temp = gTTS(text=" ", lang='en', slow=False)
		temp.save("vocals.mp3")
		sounds.append(AudioSegment.from_mp3("vocals.mp3"))
		for line in lyr:
			if i == 0 and sounds[i].duration() < 37250:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)
			elif i == 1 and sounds[i].duration() < 36750:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)
			elif i == 2 and sounds[i].duration() < 37500:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)
			elif i == 3 and sounds[i].duration() < 3600:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)
			elif i == 4 and sounds[i].duration() < 9150:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)
			elif i == 5 and sounds[i].duration() < 3750:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)
			elif sounds[i].duration() < 28500:
				tts = gTTS(text=line, lang='en', slow=False)
				tts.save("vocals.mp3")
				sounds[i] = sounds[i] + AudioSegment.from_mp3("vocals.mp3")
				sounds[i].save("vocals.mp3")
				allLyrics.append(line)		
		texttospeech.append((AudioSegment.from_mp3("vocals.mp3") + 5))
		os.remove("vocals.mp3")
		lyr = getLyrics()
	print("")
	print("Importing instrumental...")
	instrumental = (AudioSegment.from_mp3("instrumentals/ultimate.mp3") - 10)
	print("Adding instrumental to output file...")
	songv1 = instrumental.overlay(texttospeech[0][:37250],position=16750)
	print("", end='')
	print("\rOverlaying lyrics part 1 of 6...", end='')
	songv2 = songv1.overlay(texttospeech[1][:36750],position=54860)
	print("\rOverlaying lyrics part 2 of 6...", end='')
	songv3 = songv2.overlay(texttospeech[2][:37500],position=92500)
	#songv4 = songv3.overlay(texttospeech[3][:17250],position=130500)
	#songv5 = songv4.overlay(texttospeech[4][:29000].fade_out(3000),position=148300)
	#songv5.export("rap.mp3", format="mp3")
	print("\rOverlaying lyrics part 3 of 6...", end='')
	songv4 = songv3.overlay(texttospeech[3][:3600],position=130500)
	print("\rOverlaying lyrics part 4 of 6...", end='')
	songv5 = songv4.overlay(texttospeech[4][:9150],position=134500)
	print("\rOverlaying lyrics part 5 of 6...", end='')
	songv6 = songv5.overlay(texttospeech[5][:3750],position=144250)
	print("\rOverlaying lyrics part 6 of 6...", end='')
	songv7 = songv6.overlay(texttospeech[6][:28500].fade_out(3000),position=148300)
	print("")
	print("Exporting finished song...")
	songv7.export("static/mixed_sounds.mp3", format="mp3")
	return allLyrics

if __name__ == '__main__':
	textToRap()
