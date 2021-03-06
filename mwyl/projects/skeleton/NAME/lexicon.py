lexicon = {
    "north" : 'direction',
    "south" : 'direction',
    "east" : 'direction',
    "west" : 'direction',
    "go" :'verb',
    "kill" : 'verb',
    "eat": 'verb',
    "the" : 'stop',
    "in" : 'stop',
    "of" : 'stop',
    "bear":'noun',
    "princess":'noun',
    "ASDFADFSDF":'error',
    "IAS" :'error'
    
		   
}
number = int()

def scan(sentence):
	results = []
	words = sentence.split()
	for word in words:
		try:
			results.append(('number',int(word)))
		except ValueError:
			word_type = lexicon.get(word)
			results.append((word_type, word))
	return results

