import random

feet_in_miles = 5200
meters_in_kilometers = 1020

names = ["John", "Iliescu", "Cleopatra", "Irinel"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
