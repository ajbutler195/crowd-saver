class Person:
    granularity = 20

    def __init__(self, pos0, target):
        self.position = pos0
        self.target = target
        self.velocity = vector(self)

    def vector(self):
        return (self.target[0] - self.position[0], self.target[1] - self.position[1])

    def move(self):
        self.position = (self.position[0] + (self.velocity[0] / granularity), self.position[1] + (self.veclocity[1] / granularity))
        return self.position
        

    
    