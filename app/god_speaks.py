import os
from pydub import AudioSegment
from gtts import gTTS
from god_rap import get_lyrics

def text_to_rap():
	result = []
	song = (AudioSegment.from_mp3("instrumentals/ultimate.mp3") - 10)
	offset = 16750
	for i in range(0,5):
		lyr = get_lyrics()
		for line in lyr:
			tts = gTTS(text=line, lang='en', slow=False)
			tts.save("vocals.mp3")
			bar = (AudioSegment.from_mp3("vocals.mp3") + 5)
			if i == 0 and (offset + len(bar)) <= 54860:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 0:
				cut = 54050 - offset
				song = song.overlay(bar[:cut],position=offset)
				result.append(line)
				offset = 54860
				break
			elif i == 1 and (offset + len(bar)) <= 92500:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 1:
				cut = 91610 - offset
				song = song.overlay(bar[:cut],position=offset)
				result.append(line)
				offset = 92500
				break
			elif i == 2 and (offset + len(bar)) <= 130500:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 2:
				cut = 130000 - offset
				song = song.overlay(bar[:cut],position=offset)
				result.append(line)
				offset = 130500
				break
			elif i == 3 and (offset + len(bar)) <= 148300:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 3:
				cut = 148000 - offset
				song = song.overlay(bar[:cut],position=offset)
				result.append(line)
				offset = 148300
				break
			elif i == 4 and (offset + len(bar)) <= 175800:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
				if (offset + len(bar) > 175800):
					continue
			elif i == 4:
				song = song.overlay(bar.fade_out(3000),position=offset)
				result.append(line)
				break
		result[-1] += "\n"
	os.remove("vocals.mp3")
	song.export("static/ultimate_rap.mp3", format="mp3")
	return result

if __name__ == '__main__':
	final_song = text_to_rap()
	for i in range(len(final_song)):
		print(final_song[i])
