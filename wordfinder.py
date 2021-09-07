from random import randint


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """create word_finder from path, call read_words function"""

        self.path = path
        self.read_words()

    def __repr__(self):
        return f"WordFinder run at path {self.path}"

    def read_words(self):
        """read file, create list of words in file, and return string of number of words read"""
        file = open(self.path, "r")
        self.words = file.readlines()
        self.words = [word.replace(
            "\n", "") if word.endswith("\n") else word for word in self.words]
            # strip
        print(f"{len(self.words)} words read")

    def random(self):
        """pick a random word from list of words"""
        random_int = randint(0, len(self.words)-1)
        return self.words[random_int]

class RandomWordFinder(WordFinder):
    """Subclass of WordFinder where comments and lines are parsed out"""

    def __init__(self, path):
        super().__init__(path)
    
    def read_words(self):
        """Read file and create list of words in file but ignore comments and line breaks. 
        Returns number of words read"""
        super().read_words()
        self.words = [word for word in self.words if not word.startswith("#") and word != ""]

