"""Word Finder: finds random words from a dictionary."""

import random

# need to import 'random' built in functions
#
# had to read solution on how to create this one


class WordFinder:
    """class for finding random words from a file of words

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in ["Aani", "Aaron", "abandon"]
    True

    >>> wf.random() in ["accoy", "acedy", "acetum"]
    """

    def __init__(self, path):
        """shows how many items were read"""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)
