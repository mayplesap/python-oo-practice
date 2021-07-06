from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_name):
        """ Initializes file_name and a list of words from file_name. """
        self.file_name = file_name 
        file = open(self.file_name)
        self.words = self.create_list(file)
        print(f"{len(self.words)} words read")
        file.close()
        #list of words, better name


    def create_list(self, file):
        """ Appends to a list, returns list of words. """
        words = [line.strip() for line in file]
        
        return words


    def random(self):
        """ Return a random word from list. """
        word = choice(self.words)
        return word


class SpecialWordFinder(WordFinder):
    """ Finds random words from a dictionary, 
        excludes blank lines and # symbol. """

    def create_list(self, file):
        """ Create a list without blank lines and comments(#). """
        words = [line.strip() for line in file 
                    if line.strip() != "" and not line.startswith("#")]

        return words


# wf = SpecialWordFinder("input file name here")

# print(wf.random())
# print(wf.random())
# print(wf.random())
# print(wf.random())
# print(wf.random())
# print(wf.random())
# print(wf.random())
# print(wf.random())

