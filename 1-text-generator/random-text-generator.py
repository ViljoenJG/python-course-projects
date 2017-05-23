import random

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = vowels + consonants

str_cnt = int(input('How many strings should I generate? '))
str_len = int(input('How long should the string(s) be? '))
str_entries = []

for a in range(str_len):
    str_entries.append(input(str(a + 1) + ". Enter 'c' for consonant, 'v' for vowel and 'l' for any:  "))


def generate_string():
    generated = ''

    for entry in str_entries:
        if entry == 'l':
            generated += random.choice(letters)
        elif entry == 'c':
            generated += random.choice(consonants)
        elif entry == 'v':
            generated += random.choice(vowels)
        else:
            generated += entry

    return generated

for b in range(str_cnt):
    print(generate_string())
