class Person:
    def __init__(self, pos0, target):
        self.position = pos0
        self.target = target
        self.velocity = vector(self)

    def vector(self):
        return (self.position[0] - self.target[0], self.position[1] - self.target[1])

    