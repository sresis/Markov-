"""Generate Markov text from text files."""

from random import choice

import sys
n_nome = int(input('Please input n-nome size: '))

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

    for i in range(len(words) - n_nome):
        nnome_key = (words[i],)
        j = i + 1
        while j < (n_nome + i):
            nnome_key = nnome_key + (words[j],)
            j += 1
    
        if nnome_key not in chains.keys():
            chains[nnome_key] = []           
        chains[nnome_key].append(words[i + n_nome])
    return chains


def make_text(chains):
    """Return text from chains."""
  # maybe make a function and re-refernece
    
    # this will start at random point in choice dict
    key_val = choice(list(chains.keys()),)
    # add on to list which each word pair
    words_list = []
    i = 0
    while i < n_nome:
        words_list.append(key_val[i])
        i += 1

    #new word to be selected (from values in dict)
    new_word = choice(chains[key_val])
    final_key = ()

    # updates keys and searches for value, until key not in dict    
    while new_word is not None:
        i = 1
        final_key = ()
        while i < (n_nome ):
            final_key = final_key + (key_val[i],)
            i += 1
        final_key = final_key + (new_word,)

        words_list.append(new_word)
        if final_key in chains.keys():
            new_word = choice(chains[final_key])
            key_val = final_key
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
