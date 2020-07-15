"""Generate Markov text from text files."""

from random import choice

import sys
file = open(sys.argv[1])

def open_and_read_file(file):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file).read()


    return contents


def make_chains(contents):
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

    words = contents.split()

    for i in range(len(words) - 2):
        new_pair = (words[i], words[i + 1])
        if new_pair not in chains.keys():
            chains[new_pair] = []           
        chains[new_pair].append(words[i + 2])
  
    return chains

def make_text(chains):
    """Return text from chains."""
  # maybe make a function and re-refernece
    
    # this will start at random point in choice dict
    key_val = choice(list(chains.keys()))
    # add on to list which each word pair
    words_list = [key_val[0], key_val[1]]
    #new word to be selected (from values in dict)
    new_word = choice(chains[key_val])


    # add to list while keys are valid
    while new_word is not None:
        key_val = (key_val[1], new_word)
        words_list.append(new_word)
        if key_val in chains.keys():
            new_word = choice(chains[key_val])
        else:
            final_list = " ".join(words_list)
            return final_list
  
     

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
