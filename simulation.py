import math
from dot import Person
import random
import numpy as np

BOX_WIDTH = 10
BOX_HEIGHT = 10
count = 0

def run_simulation_tick(people):
    for person in people:
        person.move()
        handle_box_collision(person)
        print(str(person.id) + "," + str(person.position[0]) + "," + str(person.position[1]))

    handle_collisions(people)
    print("STOP")


def generate_person() -> Person:
    global count
    result = Person(count, (random.randint(4, 6), 0), (random.randint(3, 7), 10), random.randint(160, 180))
    count += 1
    return result

def generate_people():
    people = []
    for i in range(4):
        people.append(generate_person())
    return people

def handle_box_collision(person):
    # Bottom and top.
    if person.position[1] <= 0 or person.position[1] >= BOX_HEIGHT:
        person.velocity = (person.velocity[0], -person.velocity[1])
        person.move()
    # Left and side.
    if person.position[0] <= 0 or person.position[0] >= BOX_WIDTH:
        person.velocity = (-person.velocity[0], person.velocity[1])
        person.move() 

def handle_collisions(people):
    # Non-optimal solution, i.e. n^2
    for person in people:
        for other_person in people:
            if person.id != other_person.id and vector_distance_2d(person.position, other_person.position) <= Person.radius*2:
                #Collision
                v1, v2 = get_response_velocities(person, other_person)
                person.velocity = v1
                other_person.velocity = v2
                person.move()
                other_person.move()



def get_response_velocities(particle, other_particle):
    # https://en.wikipedia.org/wiki/Elastic_collision
    v1 = particle.velocity
    v2 = other_particle.velocity
    m1 = particle.mass
    m2 = other_particle.mass
    x1 = particle.position
    x2 = other_particle.position

    particle_response_v = compute_velocity(v1, v2, m1, m2, x1, x2)
    other_particle_response_v = compute_velocity(v2, v1, m2, m1, x2, x1)
    return particle_response_v, other_particle_response_v

def compute_velocity(v1, v2, m1, m2, x1, x2):
    #ref = np.array([[v1[0], v1[1]], [v2[0], v2[1]], [x1[0], x1[1]], [x2[0], x2[1]]])
    #comp = np.array([v1[0], v1[1]] - (2 * m2 / (m1 + m2)) * np.dot([v1[0] - v2[0], v1[1] - v2[1]], [x1[0] - x2[0], x1[1]-x2[1]]) / np.linalg.norm([x1[0] - x2[0], x1[1]-x2[1]]) ** 2 * ([x1[0] - x2[0], x1[1]-x2[1]])
    #comp22 = v1[1] - (2 * m2 / (m1 + m2)) * np.dot(v1[1] - v2[1], x1[1] - x2[1]) / np.linalg.norm(x1[1] - x2[1]) ** 2 * (x1[1] - x2[1])
    comp_1 = v1[0] - (2 * m2 / (m1 + m2)) * np.dot(sub2d(v1, v2), sub2d(x1, x2)) / norm_2d(sub2d(x1,x2)) ** 2 * (x1[0] - x2[0])
    comp_2 = v1[1] - (2 * m2 / (m1 + m2)) * np.dot(sub2d(v1, v2), sub2d(x1, x2)) / norm_2d(sub2d(x1,x2)) ** 2 * (x1[1] - x2[1])
    return comp_1, comp_2

def sub2d(a, b):
    return (a[0]-b[0], a[1]-b[1])

def norm_2d(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def vector_distance_2d(a,b):
    alpha = (a[0]-b[0])**2
    beta = (a[1]-b[1])**2
    return math.sqrt(alpha + beta)


if __name__ == "__main__":
    people = [generate_person()]
    ticks = 60
    for tick in range(ticks):
        run_simulation_tick(people)
        people.append(generate_person())