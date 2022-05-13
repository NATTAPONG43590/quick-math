#import python libraries for number game
from ast import While, operator
import random
import glob
import time
from tkinter.messagebox import QUESTION
import numpy as np
import tkinter
import turtle
import os
import pygame
from random import randint, uniform, choice
import math
from win32gui import SetWindowPos

#================================ initial variable setup ==================================
score = 0 #initialize score

time_per_question = 30 #initialize time per question
additional_time = 1 #time added per correct answer
terms = np.array(["+","-","x","/"]) #initialize terms
ranges = np.array([[1,9],[1,9],[1,10],[2,10]]) #add sub mul div
#================================= function for game =======================================
class Quiz:
    
    def __init__(self):
        self.terms_range = 2#random.randint(2,6)
        self.operators = np.array([])
        self.operands = np.array([]) 
        self.operands = np.append(self.operands,int(random.randint(ranges[0][0],ranges[0][1])))
        for i in range(self.terms_range-1):
            self.operators = np.append(self.operators,int(random.randint(0,len(terms)-3)))
            self.operands = np.append(self.operands,int(random.randint(ranges[int(self.operators[i])][0],ranges[int(self.operators[i])][1])))
            # while self.operators[i] == 3 and i > 0 :
            #     print(self.operands[i-1] , " % ", self.operands[i] , " = " , self.is_divisible(self.operands,i-1,i ))
            #     print(self.operands , i)
            #     print(self.operators)
            #     if self.is_prime(int(self.operands[i-1])):
            #         self.operators[i] = int(random.randint(0,len(terms)-2))
            #         break
            #     elif not self.is_divisible(self.operands,i-1,i):
            #         self.operands[i] = int(random.randint(ranges[int(self.operators[i])][0],ranges[int(self.operators[i])][1]))

            #     print(self.operands)
            #     print(self.operators)
            # #if value is undivisible by previous value, then change it
            #     if self.is_divisible(self.operands,i-1,i):break
    @ classmethod
    def is_prime(self,n):
        if n == 1:
            return False
        for x in range(2,n):
            if n % x == 0:
                return False
        else:
            return True
    def is_divisible(self,arr,n1,n2):
        if (float(arr[n1]) % float(arr[n2]) == 0):
            return True
        return False
        
      
#================================= main function ===========================================
while True:
    q = Quiz()
    def check_answer(ans):
        answer = q.operands[0]
        for i in range(1,len(q.operands)):
            if(q.operators[i-1] == 0):
                answer += q.operands[i]
            elif(q.operators[i-1] == 1):
                answer -= q.operands[i]
            elif(q.operators[i-1] == 2):
                answer *= q.operands[i]
            elif(q.operators[i-1] == 3):
                answer /= q.operands[i]
        if(int(ans) == int(answer)):
            return True
        return answer

  
    question = "\033[41m" + "question : " 
    for i in range(len(q.operands-1)):
        if i == 0:
            question += str(int(q.operands[0])) + " "
        else:
            question += terms[int(q.operators[i-1])] + " "
            question += str(int(q.operands[i])) + " "
    question += "\033[0m"
    print(question) 
    #get user input
    start = time.time()
    ans = input("Enter your answer: ")
    os.system('CLS')
    sec = time.time()
    time_taken = sec - start
    sec = start = 0
    if(check_answer(ans) == True):
        score += 1
        print('\033[32m'+"Correct! " + '\033[0m')
        print("your score is: ", score)
        
        
    else:
        print("Incorrect! the answer is: ", int(check_answer(ans)))
        print("your score is: ", score)
        break
    print("time taken: ", round(time_taken,2))
    question = ""
    
    if(score == 1):

        # screen = turtle.Screen()
        
        # rootwindow = screen.getcanvas().winfo_toplevel()
        # rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        # rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        # screen.bgcolor("black")
        # screen.colormode(255)
        # t = turtle.Turtle()
        # t.speed(10000)
        # # BONUS: ADD STARS! -----------
        
        # for i in range(20):
        #     x = random.randint(-250, 250)
        #     y = random.randint(-250,250)
        #     t.penup()
        #     t.goto(x,y)
        #     t.pendown()
        #     rs = int(random.randint(0, 255))
        #     gs = int(random.randint(0, 255))
        #     bs = int(random.randint(0, 255))
        #     t.color(rs,gs,bs)
        #     size = random.randint(2, 8)
        #     for i in range(5):
        #         t.forward(size)
        #         t.backward(size)
        #         t.left(72)
        # #--------------------------------

        # for i in range(30):

        #   x = random.randint(-250, 250)
        #   y = random.randint(-250,250)
        #   t.penup()
        #   t.goto(x,y)
        #   t.pendown()

        #   r = int(random.randint(0, 255))
        #   g = int(random.randint(0, 255))
        #   b = int(random.randint(0, 255))
        #   t.color(r, g, b)

        #   size = random.randint(30, 200)
        #   for i in range(36):
        #     t.forward(size)
        #     t.backward(size)
        #     t.left(10)
        vector2 = pygame.math.Vector2
        trails = []
        fade_p = []

        # general
        GRAVITY_FIREWORK = vector2(0, 0.3)
        GRAVITY_PARTICLE = vector2(0, 0.07)
        DISPLAY_WIDTH = DISPLAY_HEIGHT = 800
        BACKGROUND_COLOR = (20, 20, 30) 
        # firework
        FIREWORK_SPEED_MIN = 17
        FIREWORK_SPEED_MAX = 20
        FIREWORK_SIZE = 2
        # particle
        PARTICLE_LIFESPAN = 70
        X_SPREAD = 0.8
        Y_SPREAD = 0.8
        PARTICLE_SIZE = 4
        MIN_PARTICLES = 100
        MAX_PARTICLES = 200
        X_WIGGLE_SCALE = 20  # higher -> less wiggle
        Y_WIGGLE_SCALE = 10
        EXPLOSION_RADIUS_MIN = 10
        EXPLOSION_RADIUS_MAX = 25
        COLORFUL = True
        # trail
        TRAIL_LIFESPAN = PARTICLE_LIFESPAN / 2
        TRAIL_FREQUENCY = 5  # higher -> less trails
        TRAILS = True
        #FADE_COLOURS = [(45, 45, 45), (60, 60, 60), (75, 75, 75), (125, 125, 125), (150, 150, 150)]


        class Firework:
            def __init__(self):
                self.colour = tuple(randint(0, 255) for _ in range(3))
                self.colours = tuple(tuple(randint(0, 255) for _ in range(3)) for _ in range(3))
                # Creates the firework particle
                self.firework = Particle(randint(0, DISPLAY_WIDTH), DISPLAY_HEIGHT, True, self.colour)
                self.exploded = False
                self.particles = []

            def update(self, win: pygame.Surface) -> None:
                # method called every frame
                if not self.exploded:
                    self.firework.apply_force(GRAVITY_FIREWORK)
                    self.firework.move()
                    self.show(win)
                    if self.firework.vel.y >= 0:
                        self.exploded = True
                        self.explode()

                else:
                    for particle in self.particles:
                        particle.update()
                        particle.show(win)

            def explode(self):
                # when the firework has entered a stand still, create the explosion particles
                amount = randint(MIN_PARTICLES, MAX_PARTICLES)
                if COLORFUL:
                    self.particles = [Particle(self.firework.pos.x, self.firework.pos.y, False, choice(self.colours)) for _ in range(amount)]
                else:
                    self.particles = [Particle(self.firework.pos.x, self.firework.pos.y, False, self.colour) for _ in range(amount)]

            def show(self, win: pygame.Surface) -> None:
                # draw the firework on the given surface
                x = int(self.firework.pos.x)
                y = int(self.firework.pos.y)
                pygame.draw.circle(win, self.colour, (x, y), self.firework.size)

            def remove(self) -> bool:
                if not self.exploded:
                    return False

                for p in self.particles:
                    if p.remove:
                        self.particles.remove(p)

                # remove the firework object if all particles are gone
                return len(self.particles) == 0


        class Particle(object):
            def __init__(self, x, y, firework, colour):
                self.firework = firework
                self.pos = vector2(x, y)
                self.origin = vector2(x, y)
                self.acc = vector2(0, 0)
                self.remove = False
                self.explosion_radius = randint(EXPLOSION_RADIUS_MIN, EXPLOSION_RADIUS_MAX)
                self.life = 0
                self.colour = colour
                self.trail_frequency = TRAIL_FREQUENCY + randint(-3, 3)

                if self.firework:
                    self.vel = vector2(0, -randint(FIREWORK_SPEED_MIN, FIREWORK_SPEED_MAX))
                    self.size = FIREWORK_SIZE
                else:
                    # set random position of particle 
                    self.vel = vector2(uniform(-1, 1), uniform(-1, 1))
                    self.vel.x *= randint(7, self.explosion_radius + 2)
                    self.vel.y *= randint(7, self.explosion_radius + 2)
                    self.size = randint(PARTICLE_SIZE - 1, PARTICLE_SIZE + 1)
                    # update pos and remove particle if outside radius
                    self.move()
                    self.outside_spawn_radius()

            def update(self) -> None:
                # called every frame
                self.life += 1
                # add a new trail if life % x == 0
                if self.life % self.trail_frequency == 0:
                    trails.append(Trail(self.pos.x, self.pos.y, False, self.colour, self.size))
                # wiggle
                self.apply_force(vector2(uniform(-1, 1) / X_WIGGLE_SCALE, GRAVITY_PARTICLE.y + uniform(-1, 1) / Y_WIGGLE_SCALE))
                self.move()

            def apply_force(self, force: pygame.math.Vector2) -> None:
                self.acc += force

            def outside_spawn_radius(self) -> bool:
                # if the particle spawned is outside of the radius that creates the circular firework, remov it
                distance = math.sqrt((self.pos.x - self.origin.x) ** 2 + (self.pos.y - self.origin.y) ** 2)
                return distance > self.explosion_radius

            def move(self) -> None:
                # called every frame, moves the particle
                if not self.firework:
                    self.vel.x *= X_SPREAD
                    self.vel.y *= Y_SPREAD

                self.vel += self.acc
                self.pos += self.vel
                self.acc *= 0

                self.decay()

            def show(self, win: pygame.Surface) -> None:
                # draw the particle on to the surface
                x = int(self.pos.x)
                y = int(self.pos.y)
                pygame.draw.circle(win, self.colour, (x, y), self.size)

            def decay(self) -> None:
                # random decay of the particles
                if self.life > PARTICLE_LIFESPAN:
                    if randint(0, 15) == 0:
                        self.remove = True
                # if too old, begone
                if not self.remove and self.life > PARTICLE_LIFESPAN * 1.5:
                    self.remove = True


        class Trail(Particle):
            def __init__(self, x, y, is_firework, colour, parent_size):
                Particle.__init__(self, x, y, is_firework, colour)
                self.size = parent_size - 1

            def decay(self) -> bool:
                # decay also changes the color on the trails
                # returns true if to be removed, else false
                self.life += 1
                if self.life % 100 == 0:
                    self.size -= 1

                self.size = max(0, self.size)
                # static yellow-ish colour self.colour = (255, 255, 220)
                self.colour = (min(self.colour[0] + 5, 255), min(self.colour[1] + 5, 255), min(self.colour[2] + 5, 255))

                if self.life > TRAIL_LIFESPAN:
                    ran = randint(0, 15)
                    if ran == 0:
                        return True
                # if too old, begone
                if not self.remove and self.life > TRAIL_LIFESPAN * 1.5:
                    return True

                return False


        def update(win: pygame.Surface, fireworks: list, trails: list) -> None:
            if TRAILS:
                for t in trails:
                    t.show(win)
                    if t.decay():
                        trails.remove(t)

            for fw in fireworks:
                fw.update(win)
                if fw.remove():
                    fireworks.remove(fw)

            pygame.display.update()


        def main():
            pygame.init()
            pygame.display.set_caption("Fireworks in Pygame")
            win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
            clock = pygame.time.Clock()

            SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 1)
            fireworks = [Firework() for i in range(1)]  # create the first fireworks
            running = True

            while running:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            fireworks.append(Firework())
                        elif event.key == pygame.K_2:
                            for i in range(10):
                                fireworks.append(Firework())
                win.fill(BACKGROUND_COLOR)  # draw background

                if randint(0, 70) == 1:  # create new firework
                    fireworks.append(Firework())

                update(win, fireworks, trails)

                # stats for fun
                # total_particles = 0
                # for f in fireworks:
                #    total_particles += len(f.particles)

                # print(f"Fireworks: {len(fireworks)}\nParticles: {total_particles}\n\n")

            pygame.quit()
            quit()


        main()
