class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0): #set default
        """DOCSTRINGS"""
        self.original_start = self.start = start
        #self.start could be named current_num or something more specific
    
    # __repr__

    def generate(self):
        """DOCSTRINGS"""
        self.start += 1
        return self.start - 1
    
    def reset(self):
        """DOCSTRINGS"""
        self.start = self.original_start