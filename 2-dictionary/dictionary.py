import json
from difflib import get_close_matches


def print_definition(word_def):
    if type(word_def) == list:
        for wd in word_def:
                print('- {0}'.format(wd))
    else:
        print(word_def)


def get_close(w, data):
    possible_matches = get_close_matches(w, data.keys(), cutoff=0.8)
    if len(possible_matches) > 0:
        yn = input("Not found. Did you mean {0}? [y/n]".format(possible_matches[0])).upper()
        if yn == "Y":
            return data[possible_matches[0]]
        elif yn == "N":
            return "Unable to find definition."
        else:
            return "Invalid input."
    
    return "Unable to find definition."


data = json.load(open("data.json"))
word = input("Enter word: ")

if word in data:
    print_definition(data[word])
elif word.lower() in data:
    print_definition(data[word.lower()])
else:
    print_definition(get_close(word.lower(), data))
