#Program partitions song urls into different files, song a divide and conquer approach can be used to gather lyric data
f = open('Lyrics Websites.txt')
counter = 0
fileNum = 1
name = "URLS" + str(fileNum) + ".txt"
for url in f:
	if counter%500 == 0 and not counter == 0:
		g.close()
		name = "URLS"
		name = name[-1:] + str(fileNum) + ".txt"
		g = open(name, 'w')
		fileNum+=1
	elif counter == 0:
		g = open(name, 'w')
		fileNum+=1
	g.write("%s"%url)
	counter+=1
g.close()
