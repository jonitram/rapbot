aList = ['aaaaa']
out_text = open("CurrentSorted.txt", 'w')
for url in open('Current.txt', 'r', encoding='utf-8-sig'):
	aList.append(url)
aList.sort()
for url in aList:
	out_text.write("%s"%url)
out_text.close()
