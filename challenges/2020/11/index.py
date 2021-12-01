import numpy as np
import copy

class Challenge():
    def __init__(self, data):
        self.input = data.split()
        for i in range(len(self.input)):
            self.input[i] = list(self.input[i])
        self.show()
        
        


    def star1(self):
        previous = []
        while sorted(previous) != sorted(self.input):
            previous = self.input.copy()
            self.applyRules1()
            self.show()

        return [item for items in self.input for item in items].count('#')

    def star2(self):
        previous = []
        while sorted(previous) != sorted(self.input):
            previous = self.input.copy()
            self.applyRules2()
            self.show()

        return [item for items in self.input for item in items].count('#')
    
    def applyRules1(self):
        result = copy.deepcopy(self.input)
        for y in range(len(result)): # rows
            for x in range(len(result[y])): # seats
                #print(x, y)
                seat = self.getSeat(x, y )
                if self.hasNoOccupiedSeatsAround1(x, y) and seat == 'L':
                    result[y][x] = '#'
                if self.isTooCrowded1(x, y) and seat == '#':
                    result[y][x] = 'L'

        self.input = result
        return result

    def applyRules2(self):
        result = copy.deepcopy(self.input)
        for y in range(len(result)): # rows
            for x in range(len(result[y])): # seats
                #print(x, y)
                seat = self.getSeat2(x, y)
                if self.hasNoOccupiedSeatsAround2(x, y) and seat == 'L':
                    result[y][x] = '#'
                if self.isTooCrowded2(x, y) and seat == '#':
                    result[y][x] = 'L'

        self.input = result
        return result

    def show(self):
        print('-------------------------------')
        for line in self.input:
            print(line)
        print('-------------------------------')

    def getSeat(self, x,y):
        if x < 0 or y < 0:
            return '.'

        try:
            res = self.input[y][x]
            return res
        except IndexError as err:
            return '.'

    def getSeat2(self, x,y):
        if x < 0 or y < 0:
            return None

        try:
            res = self.input[y][x]
            return res
        except IndexError as err:
            return None

    def hasNoOccupiedSeatsAround1(self, x ,y):
        resArr = []
        for xOffset in range(-1, 2):
            for yOffset in range(-1, 2):
                seat = self.getSeat(x + xOffset, y + yOffset)
                #print(seat, xOffset, yOffset)
                resArr.append(seat == 'L' or seat == '.')
        return np.all(resArr)

    def isTooCrowded1(self, x ,y):
        resArr = []
        for xOffset in range(-1, 2):
            for yOffset in range(-1, 2):
                seat = self.getSeat(x + xOffset, y + yOffset)
                resArr.append(seat)
        return resArr.count('#') > 4


    def hasNoOccupiedSeatsAround2(self, x ,y):
        resArr = []

        dirs = [[-1, 0], [0, -1], [-1,-1], [1,0], [0, 1], [1,1], [-1, 1], [1, -1]]

        for dir in dirs:
            seat = self.getSeatByDirection(x + dir[0], y + dir[1], dir[0] , dir[1])
            #print(seat, xOffset, yOffset)
            resArr.append(seat == 'L' or seat == '.')
        return np.all(resArr)

    def isTooCrowded2(self, x ,y):
        resArr = []

        dirs = [[-1, 0], [0, -1], [-1,-1], [1,0], [0, 1], [1,1], [-1, 1], [1, -1]]

        for dir in dirs:
            seat = self.getSeatByDirection(x + dir[0], y + dir[1], dir[0] , dir[1])
            #print(f'Seat {x} {y} saw {seat} in direction {dir}')
            resArr.append(seat)
        return resArr.count('#') >= 5

    def getSeatByDirection(self, x, y, origX, origY):
       #print( x, y, origX, origY)


       if y > len(self.input[0]) or y < 0:
           return 'L'
       if x > len(self.input) or x < 0:
           return 'L'

       seat = self.getSeat2(x, y)
       if seat == 'L' or seat == '#':
           return seat
       else: 
           return self.getSeatByDirection(x + origX, y + origY, origX, origY) 
