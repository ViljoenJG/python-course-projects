import json
import difflib
from difflib import get_close_matches

def print_definition(w, data):
    if w in data:
        for d in data[w]:
            print('- {0}'.format(d))
    else:
        possibleMatches = get_close_matches(w, data.keys())
        if len(possibleMatches) > 0:
            print("Unable to find word, possible matches: ")
            for s in possibleMatches:
                print(s)
        else:
            print("Cannot find definition for the word. Please make sure it is correct.")


data = json.load(open("data.json"))
word = input("Enter word: ").lower()
print_definition(word, data)