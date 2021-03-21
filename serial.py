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

    def __init__(self, start=0):
        """Make a new gen, with the start at start"""

        self.start = self.next = start

    def __repr__(self):
        """Representation that is much clearer to read than the standard return"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Returns the next serial"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset to start"""

        self.next = self.start
