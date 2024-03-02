class Person:
    def __init__(self, pos0, target):
        self.position = pos0
        self.target = target
        self.velocity = vector(self)

    def vector(self):
        