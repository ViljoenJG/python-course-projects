import random

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = vowels + consonants

str_cnt = int(input('How many strings should I generate? '))
str_len = int(input('How long should the string(s) be? '))
str_entries = []

for ent in range(str_len):
    str_entries.append(input("Char %d. Enter 'c' for consonant, 'v' for vowel and 'l' for letter:  " % (ent + 1)))


def generate_string():
    generated = []

    for entry in str_entries:
        if entry == 'l':
            generated.append(random.choice(letters))
        elif entry == 'c':
            generated.append(random.choice(consonants))
        elif entry == 'v':
            generated.append(random.choice(vowels))
        else:
            generated.append(entry)

    return ''.join(generated)

for i in range(str_cnt):
    print('Result %d: %s' % (i + 1, generate_string()))
