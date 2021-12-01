class Challenge():
    def __init__(self, data):
        self.input = list(map(lambda x: int(x), data.split(',')))
        print(self.input)
        self.next = 0
        self.spoken = {}

    def star1(self):
        i = 1
        for x in self.input:
            self.spoken[x] = i
            i += 1

        while i <= 2020:
            current = self.next
            if current in self.spoken:
                self.next = i - self.spoken[current]
            else:
                self.next = 0
            self.spoken[current] = i
            i +=1
        return current

    def star2(self):
        i = 1
        for x in self.input:
            self.spoken[x] = i
            i += 1

        while i <= 30000000:
            current = self.next
            if current in self.spoken:
                self.next = i - self.spoken[current]
            else:
                self.next = 0
            self.spoken[current] = i
            i +=1
        return current
