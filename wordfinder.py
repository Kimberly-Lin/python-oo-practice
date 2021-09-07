from random import randint


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """create word_finder from path, call read_words function"""

        self.path = path
        self.read_words()
        print(f"{len(self.words)} words read")

    def __repr__(self):
        """returns string that shows file path"""
        return f"WordFinder run at path {self.path}"

    def read_words(self):
        """read file, create list of words in file set as class attribute words"""
        file = open(self.path, "r")
        self.words = file.readlines()
        self.words = [word.strip() for word in self.words]

    def random(self):
        """pick a random word from list of words"""
        random_int = randint(0, len(self.words)-1) #could use choice here instead of randint
        return self.words[random_int]

class RandomWordFinder(WordFinder):
    """Subclass of WordFinder where comments and lines are parsed out"""

    # def __init__(self, path):
    #     """initiate"""
    #     #don't need this! It's the same as the parent so if 
    #     #it doesn't exist in the subclass, it would go to parent to find init
    #     super().__init__(path) 

    def read_words(self):
        """Read file and create list of words in file but ignore comments and line breaks. 
        Returns number of words read"""
        super().read_words()
        self.words = [word for word in self.words if not word.startswith("#") and word != ""]

