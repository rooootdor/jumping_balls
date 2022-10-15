import random
import time

import pygame
from threading import Thread

pygame.init()

display_width, display_height = 800, 600
screen = pygame.display.set_mode([display_width, display_height])
back_color = (225, 225, 225)
screen.fill(back_color)
time.sleep(3)


# get input from player:
circles_num = int(input("Please enter the wanted circle numbers: "))


class Circle:
    display_width, display_height = 800, 600
    counter_of_balls = 0

    def __init__(self):
        self.Circle_surface = screen
        self.Circle_color = self.generate_color()
        self.Circle_radius = 10
        self.Circle_pos = (25, 25)
        self.Circle_jumps = self.generate_num_of_jumps()
        self.Circle_width = 0
        Circle.counter_of_balls += 1

    # -----
    # needed args & functions for later->
    def character(self):
        pygame.draw.circle(self.Circle_surface, self.Circle_color, self.Circle_pos, self.Circle_radius,
                           self.Circle_width)

    @staticmethod
    def generate_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        return rgb

    @staticmethod
    def generate_num_of_jumps():
        return random.randint(2, 20)

    def generate_pos(self):
        x = random.randint(self.Circle_radius, (Circle.display_width - self.Circle_radius))
        y = random.randint(self.Circle_radius, (Circle.display_height - self.Circle_radius))
        self.Circle_pos = (x, y)

    def move_pos(self):
        self.Circle_jumps = self.Circle_jumps - 1
        self.generate_pos()

    def print_num_of_circles(self):
        print('number of circles on scrn is - ', Circle.circles_num)

    def move_ball(self):
        while self.Circle_jumps > 0:
            # draw ball in new pos
            self.move_pos()
            self.character()
            pygame.display.update()
            time.sleep(0.1)  # Sleep for 3 seconds

            # "clear" location of ball:
            ball_colore = self.Circle_color
            self.Circle_color = back_color
            self.character()
            pygame.display.update()
            self.Circle_color = ball_colore

            print("number of junps left", self.Circle_jumps)

            # after ball "died"
        Circle.counter_of_balls = Circle.counter_of_balls - 1
        print("now only", Circle.counter_of_balls, "balls")

# ----
# --

threads = []
for circle in range(circles_num):
    print("new circle")
    new_Circle = Circle()

    t = Thread(target=Circle.move_ball, args=(new_Circle,))
    threads.append(t)

print("reached here")
for t in threads:
    t.start()

# Wait all threads to finish.
for t in threads:
    t.join()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # print(len(Circle.circles))

# make a thread responsible of printing the following -
# 1) ball started running
# 2) ball ended running
# 3) number of balls on the screen
