# plane = 128 rows * 8 cols
import math

f = open("./5/input.txt", "r")
input = f.read().split()


def checkSeat(seatLine):
    print(seatLine)
    rowMin = 0
    rowMax = 127
    colMax = 7
    colMin = 0
    for char in seatLine:
        if char == "B":
            if (rowMax - rowMin == 1):
                rowMin = rowMax
                pass
            else:
                rowMin += round((rowMax - rowMin) / 2)
                pass
            pass
        elif(char == "F"):
            if (rowMax - rowMin == 1):
                rowMax = rowMin
                pass
            else:
                rowMax -= round((rowMax - rowMin) / 2)
                pass
            pass
        elif(char == "L"):
            if (colMax - colMin == 1):
                colMax = colMin
                pass
            else:
                colMax -= round((colMax - colMin) / 2)
                pass
            pass
        elif(char == "R"):
            if (colMax - colMin == 1):
                colMin = colMax
                pass
            else:
                colMin += round((colMax - colMin) / 2)
                pass
            pass

    print(char, 'Seat is at row ', rowMin,
          rowMax, ' and col ', colMin, colMax)

    # min and max should be the same at this point
    return rowMin * 8 + colMin


seatIds = []
for seatLine in input:
    seatId = checkSeat(seatLine)
    seatIds.append(seatId)


print(max(seatIds))


print('----------- part2')

seatIds = sorted(seatIds)

i = 0
for seatId in sorted(seatIds):
    if (seatIds[i + 1] - seatIds[i - 1] != 2):
        print('Checking seat ', i, ' ', seatId, ' prev ',
              seatIds[i - 1], ' next ', seatIds[i + 1])
        pass
    i += 1
    pass
