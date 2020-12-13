from functools import reduce
from operator import mul, itemgetter

class Challenge():
    def __init__(self, data):
        self.input = data.splitlines()
        self.departureTime = int(self.input[0])
        self.possibleDepartures = self.input[1].split(',')
        print(self.departureTime)
        print(self.possibleDepartures)
        print('-------------')
    def star1(self):
        found = False
        checkingTime = self.departureTime
        timeToDepart = None
        busToTake = None

        while not found:
            for bus in self.possibleDepartures:
                if bus != 'x':
                    #print(f'Checking bus {bus} at {checkingTime}')
                    bus = int(bus)
                    if checkingTime % bus == 0:
                        found = True
                        timeToDepart = checkingTime
                        busToTake = bus
            checkingTime += 1
                
        return (timeToDepart - self.departureTime) * busToTake

    def star2(self):
        buses = []
        for i, t in enumerate(self.possibleDepartures):
        	if t != 'x':
        		buses.append((-i, int(t)))
        print(buses)
        ans = self.chinese_remainder_theorem(buses)
        return ans



    # Ty google :)

    def egcd(self, a, b):
	    if a == 0:
	    	return (b, 0, 1)

	    g, y, x = self.egcd(b % a, a)
	    return (g, x - (b // a) * y, y)

    def modinv(self, x, m):
    	g, inv, y = self.egcd(x, m)
    	assert g == 1, 'modular inverse does not exist'
    	return inv % m
    
    def chinese_remainder_theorem(self, equations):
    	x = 0
    	P = reduce(mul, map(itemgetter(1), equations))
    
    	for ai, pi in equations:
    		ni = P // pi
    		inv = self.modinv(ni, pi) # pow(ni, -1, pi) on Python >= 3.8
    		x = (x + ai * ni * inv) % P
    
    	return x