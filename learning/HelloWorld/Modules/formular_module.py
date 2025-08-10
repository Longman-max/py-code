class Formula:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rec_perimeter(self):
        return 2 * (self.length + self.width)

    def sqr_perimeter(self):
        return 6 * self.length


