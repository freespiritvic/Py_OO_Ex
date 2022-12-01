"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Find random words from a dictionary.

    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() using the list ['cat', 'dog', 'porcupine']
    'cat'

    >>> wf.random() using the list ['cat', 'dog', 'porcupine']
    'cat'

    >>> wf.random() using the list ['cat', 'dog', 'porcupine']
    'porcupine'

    >>> wf.random() using the list ['cat', 'dog', 'porcupine']
    'dog'
    """

    def __init__(self,source):
        """Reads words from dictionary"""
        self.source = source
        dict_file = open(source)
        self.words = self.parse(dict_file)

    def __repr__(self):
        """Show representation of words read"""
        return f'{len(self.words)} words read'

    def parse(self, dict_file):
        """Show list of words"""
        list = []
        for word in dict_file:
            list.append(word.strip())
        return list

    def random(self):
        """Return random word"""
        return random.choice(self.words)
        

class SpecialWordFinder:
    """RandomWordFinder that will not print blank lines and any comments. 

    >>> swf = SpecialWordFinder("veg_fruit.txt")
    3 words read

    >>> swf.random() using the list ["avocado", "peach", "orange"]
    True

    >>> swf.random() using the list ["avocado", "peach", "orange"]
    True

    >>> swf.random() using the list ["avocado", "peach", "orange"]
    True

    """

    def parse(self, dict_file):
        """Show list of words, except the blanks and comments"""
        return [word.strip() for word in dict_file
                if word.strip() and not word.startswith("#")]