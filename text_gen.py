from urllib.request import urlopen
from random import randint

def wordlistsum(wordlist):
	sum=0
	for word,value in wordlist.items():
		sum+=value
	return sum

def retrieveRandomword(wordlist):
	randindex=randint(1,wordlistsum(wordlist))
	for word,value in wordlist.items():
		randindex-=value
		if randindex <= 0:
			return word

def buildworddict(text):
	text = text.replace('\n',' ')
	text = text.replace('"','')
	punctuation = [',','.',';',':']
	for symbol in punctuation:
		text = text.replace(symbol, ' {} '.format(symbol))

	words = text.split(' ')
	words = [word for word in words if word != '']

	worddict={}
	for i in range(1,len(words)):
		if words[i-1] not in worddict:
			worddict[words[i-1]]={}
		if words[i] not in worddict[words[i-1]]:
			worddict[words[i-1]][words[i]]=0
		worddict[words[i-1]][words[i]] +=1
	return worddict

text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(),'utf-8')
worddict = buildworddict(text)	
length = 100
chain = ['I']
for i in range(0,length):
	newword = retrieveRandomword(worddict[chain[-1]])
	chain.append(newword)

print(' '.join(chain))