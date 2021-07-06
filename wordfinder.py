from random import choice
class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_name ):
        """"""
        self.file_name = file_name 
        self.list = self.read_and_create_list()


    def read_and_create_list(self):
        """"""
        curr_list = []
        file = open(self.file_name)
        for line in file:
            curr_list.append(line[ :-1])

        file.close()
        
        return curr_list


    def random(self):
        """"""
        word = choice(self.list)
        return word



