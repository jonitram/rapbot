urls = set()
for url in open('URLSNew2.txt', 'r', encoding='utf-8-sig'):
	if url not in urls:
		urls.add(url)
f = open('URLSCleaned2.txt', 'w')
for url in urls:
	f.write(url)
f.close()