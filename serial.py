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
        """ Create SerialGenerator with start. """
        self.start = start
        self.number = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.generate()}>"

    def generate(self):
        """ Increment number by 1. """
        self.number += 1
        return self.number

    def reset(self):
        """ Reset number back to the original start number. """
        self.number = self.start - 1


# serial = SerialGenerator(100)
# print(serial)
