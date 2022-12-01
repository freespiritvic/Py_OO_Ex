"""Python serial number generator."""

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

    def __init__(self,start=100):
        """ Generating the start at 100"""
        self.start = self.next = start

    def __repr__(self):
        """Show representation"""
        return f'<SerialGenerator start={self.start} next={self.next}>'

    def generate(self):
        """Generate the next number in the sequence"""
        self.next += 1
        return self.next
    
    def reset(self):
        """Reset the serialGenerator number back to 100"""
        self.next = self.start 

