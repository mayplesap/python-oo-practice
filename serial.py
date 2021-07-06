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

    def __init__(self, start = 0):
        """ create SerialGenerator with start """
        self.start = start
        self.number = start - 1

    def generate(self):
        """ increment number by 1 """
        self.number += 1
        return self.number

    def reset(self):
        """ reset number back to the original start number """
        self.number = self.start - 1

