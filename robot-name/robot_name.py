import string
import random


class Robot(object):
    uniqueNamesOfRobots = []

    def __init__(self):
        random.seed()
        self.name = self.create_name()

    def create_name(self):
            generated_name = ''
            assigned_unique_name = False
            while assigned_unique_name is False:
                generated_name = self.generate_name()
                if self.is_unique(generated_name):
                    assigned_unique_name = True
                    self.uniqueNamesOfRobots.append(generated_name)
            return generated_name

    @staticmethod
    def generate_name():
        first_letter = random.choice(string.ascii_uppercase)
        second_letter = random.choice(string.ascii_uppercase)
        end_of_name = random.randint(100, 1000)
        generated_name = first_letter + second_letter + str(end_of_name)
        return generated_name

    def is_unique(self, generated_name):
        if generated_name not in self.uniqueNamesOfRobots:
            return True
        else:
            return False

    def reset(self):
        self.name = self.create_name()

    def print_out(self):
        print(self.uniqueNamesOfRobots)


def test1():
    robots = []
    for i in range(10):
        robots.append(Robot())

    for i in range(10):
        print(robots[i].name, end=', ')

    robots[2].reset()
    robots[5].reset()
    print()
    for i in range(10):
        print(robots[i].name, end=', ')


if __name__ == "__main__":
    test1()





