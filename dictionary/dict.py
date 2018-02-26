import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(word):
	word = word.lower()

	if word in data:
		return data[word]

	elif word.title() in  data:
		return data[word.title()]
		
	elif  len(get_close_matches(word,data.keys())) > 0 :
		temp = input("Do you mean %s ? Press Y if yes or N if no." % get_close_matches(word,data.keys())[0])
		if temp == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif temp == "N":
			return "Please check the word entered"
		else :
			return "Please enter a valid character Y/N"

	else:
		return "Please check the word entered"


word = input("Enter Word: ")
meaning = translate(word) 

if type(meaning) == list :
	for item in meaning:
		print(item)

else:
	print(meaning)