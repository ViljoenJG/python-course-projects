import json
from difflib import get_close_matches

def check_close_and_print(w, data):
    possibleMatches = get_close_matches(w, data.keys(), cutoff=0.8)
    if len(possibleMatches) > 0:
        yn = input("Not found. Did you mean {0}? [y/n]".format(possibleMatches[0])).upper()
        if yn == "Y":
            for d in data[possibleMatches[0]]:
                print('- {0}'.format(d))
        elif yn == "N":
            print("Unable to find word, possible matches: ")
            for s in possibleMatches:
                print(s)
        else:
            print("Invalid input.")
    else:
        print("Cannot find definition for the word. Please make sure it is correct.")


def print_definition(w, data):
    if w in data:
        for d in data[w]:
            print('- {0}'.format(d))
    else:
        check_close_and_print(w, data)


data = json.load(open("data.json"))
word = input("Enter word: ").lower()
print_definition(word, data)