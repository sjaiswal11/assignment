    """ Prints combinations of words of a given word.
    """

import itertools

items = 'evell'
for i in range(len(items)+1):
    for combination in itertools.combinations(items, i): 
        print(combination)