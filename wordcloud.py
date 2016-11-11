# word cloud
#You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.
import re

def create_dictionary(str):
	dict = {}
	str = str.lower()
	str = str.replace(',',"")
	str = str.replace('?',"")
	str = str.replace('.',"")
	
	# a better way would be to split on all of the characters, including the punctuation, but re.split wasnt working
	
	tokens = re.split(' ',str)
	
	for t in tokens:
		if t in dict:
			dict[t] += 1
		else:
		    dict[t] = 1
	return dict	
s1 = 'After beating the eggs, Dana read the next step:'

s2 = 'Add milk and eggs, then add flour and sugar.'		

s3 = 'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.'

print(create_dictionary(s3))
