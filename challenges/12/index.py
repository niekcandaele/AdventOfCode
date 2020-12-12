import re
import math
import matplotlib
import matplotlib.pyplot as plt
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

windDirections = ['N', 'E', 'S', 'W']

class Challenge():
    def __init__(self, data):
        self.input = data.splitlines()
        self.directions = []
        for line in self.input:
            amount = re.findall(r'\d+', line)
            dir = re.findall(r'[^\d]+', line)
            self.directions.append([int(amount[0]), dir[0]])
        print(self.directions)
        self.trajectoryX = []
        self.trajectoryY = []
        self.direction = 'E'
        self.x = 0
        self.y = 0
        self.wayPointX = 10
        self.wayPointY = 1

    def star1(self):
        self.fly1()
        self.plot('star1')
        return self.manhattanDistance()

    def star2(self):
        self.fly2()
        self.plot('star2')
        return self.manhattanDistance()
    
    def plot(self,name):
        fig, ax = plt.subplots()
        ax.plot(self.trajectoryX, self.trajectoryY)
        ax.grid()
        fig.savefig(f"{__location__}/{name}.png")
        plt.show()

    def manhattanDistance(self):
        return abs(self.x) + abs(self.y)

    def fly1(self):
        for line in self.directions:
            self.flyRule1(line)
            self.trajectoryX.append(self.x)
            self.trajectoryY.append(self.y)
            

    def flyRule1(self, rule):
        if rule[1] == 'N':
            self.y += rule[0]
        if rule[1] == 'E':
            self.x += rule[0]
        if rule[1] == 'S':
            self.y -= rule[0]
        if rule[1] == 'W':
            self.x -= rule[0]

        if rule[1] == 'F':
            self.flyRule1([rule[0], self.direction])

        if rule[1] == 'R':
            rotation = rule[0] // 90
            currIdx = windDirections.index(self.direction)
            self.direction = windDirections[(currIdx + rotation) % 4]

        if rule[1] == 'L':
            rotation = rule[0] // 90
            currIdx = windDirections.index(self.direction)
            self.direction = windDirections[(currIdx - rotation) % 4]


    def fly2(self):
        for line in self.directions:
            self.flyRule2(line)
            self.trajectoryX.append(self.x)
            self.trajectoryY.append(self.y)

    def flyRule2(self, rule):
        if rule[1] == 'N':
            self.wayPointY += rule[0]
        if rule[1] == 'E':
            self.wayPointX += rule[0]
        if rule[1] == 'S':
            self.wayPointY -= rule[0]
        if rule[1] == 'W':
            self.wayPointX -= rule[0]

        if rule[1] == 'F':
            incrX = self.wayPointX * rule[0]
            self.x += incrX
            incrY = self.wayPointY * rule[0]
            self.y += incrY


        if rule[1] == 'L':
            for _ in range(rule[0] // 90):
                self.wayPointX, self.wayPointY = -self.wayPointY, self.wayPointX
            

        if rule[1] == 'R':
            for _ in range(rule[0] // 90):
                self.wayPointX, self.wayPointY = self.wayPointY, -self.wayPointX

        print('waypoint', self.wayPointX, self.wayPointY)