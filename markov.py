"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text:

        text = text.read()

    return text


def make_chains(text_string):
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

    words.append(None)

    index = 0

    while index < (len(words) - 2):

        if (words[index], words[index + 1]) in chains:

            chains[(words[index], words[index + 1])].append(words[index + 2])

        else:

            chains[(words[index], words[index + 1])] = [words[index + 2]]

        index += 1

    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(chains.keys())

    words = [key[0], key[1]]

    while True:

        rand_value = choice(chains[key])

        if rand_value is None:
            break

        else:
       
            words.append(rand_value)

            key = (key[1], rand_value)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
