import math
from dot import Person
from random import *
import numpy as np
import pymunk

BOX_WIDTH = 10
BOX_HEIGHT = 10

def run_simulation_tick(people):
    for person in people:
        person.move()
        handle_box_collision(person)

    handle_collisions(people)


def generate_person() -> Person:
    return Person((randint(0, 10), 0), (randint(4, 6), 11))

def generate_people():
    people = []
    for i in range(10):
        people.append(generate_person())
    return people

def handle_box_collision(person):
    # Bottom and top.
    if person.position[1] <= 0 or person.position[1] >= BOX_HEIGHT:
        particle.velocity[1] = -particle.velocity[1]
        particle.move()
    # Left and side.
    if person.position[0] <= 0 or person.position[0] >= BOX_WIDTH:
        particle.velocity[0] = -particle.velocity[0]
        particle.move() 

def handle_collisions(people):
    # Non-optimal solution, i.e. n^2
    for person in people:
        for other_person in people:
            if vector_distance_2d(person.position, other_person.position) <= Person.radius*2:
                #Collision
                v1, v2 = get_response_velocities(person, other_person)
                person.velocity = v1
                other_person.velocity = v2
                person.move()
                person.move()



def get_response_velocities(particle, other_particle):
    # https://en.wikipedia.org/wiki/Elastic_collision
    v1 = particle.velocity
    v2 = other_particle.velocity
    m1 = 1
    m2 = 1
    x1 = particle.position
    x2 = other_particle.position

    particle_response_v = compute_velocity(v1, v2, m1, m2, x1, x2)
    other_particle_response_v = compute_velocity(v2, v1, m2, m1, x2, x1)
    return particle_response_v, other_particle_response_v

def compute_velocity(v1, v2, m1, m2, x1, x2):
    ref = np.array([[v1[0], v1[1]], [v2[0], v2[1]], [x1[0], x1[1]], [x2[0], x2[1]]])
    comp = (v1[0], v1[1]) - (2 * m2 / (m1 + m2)) * np.dot((v1[0] - v2[0], v1[1] - v2[1]), (x1[0] - x2[0], x1[1]-x2[1])) / np.linalg.norm((x1[0] - x2[0], x1[1]-x2[1])) ** 2 * ((x1[0] - x2[0], x1[1]-x2[1]))
    comp_1 = v1[0] - (2 * m2 / (m1 + m2)) * np.dot(v1[0] - v2[0], x1[0] - x2[0]) / np.linalg.norm(x1[0] - x2[0]) ** 2 * (x1[0] - x2[0])
    comp_2 = v1[1] - (2 * m2 / (m1 + m2)) * np.dot(v1[1] - v2[1], x1[1] - x2[1]) / np.linalg.norm(x1[1] - x2[1]) ** 2 * (x1[1] - x2[1])
    return comp


def vector_distance_2d(a,b):
    alpha = (a[0]-b[0])**2
    beta = (a[1]-b[1])**2
    return math.sqrt(alpha + beta)


if __name__ == "__main__":
    people = generate_people()
    ticks = 20
    for tick in range(ticks):
        run_simulation_tick(people)