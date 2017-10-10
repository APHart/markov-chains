"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text:

        text = text.read()

    return text


def make_chains(text_string, n=2):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    #Adding None at the end of the list for stop flag in make_text funct.
    words.append(None)

    index = 0

    while index < (len(words) - n):

        #creates tuple of slice of words list, determined by n.
        key = tuple(words[index:index + n])

        if key in chains:

            #adding another value to the key
            chains[key].append(words[index + n])

        else:

            #adds key and value to chains dictionary
            chains[key] = [words[index + n]]

        index += 1

    return chains


def make_text(chains, n=2):
    """Return text from chains."""

    #Selects a random key from chains dictionary

    while True:
        key = choice(chains.keys())

    #only using key if it starts with a capital letter.
        if key[0].istitle():
            break

    words = []

    #Unpacks words from key tuple and adds them to words list
    for word in key:
        words.append(word)

    while True:

        #Selects random value for specified key
        rand_value = choice(chains[key])

        if rand_value is None:
            break

        else:

            #Adds word to words list
            words.append(rand_value)

            #Reassigns key to slice of original key, starting at index 1
            #(through to the end), concatenated with tuple of rand_value
            key = key[1:] + (rand_value,)

    return " ".join(words)


input_path = sys.argv[1]

n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text
