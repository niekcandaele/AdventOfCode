class Challenge():
    def __init__(self, data, preamble=25):
        self.input = list(map(lambda x: int(x), data.splitlines()))
        self.preamble = preamble

    def star1(self):
        for i in range(self.preamble, len(self.input)):
            #print(self.input[i - self.preamble:i], self.input[i])
            res = self.checkIfSumOfTail(
                self.input[i - self.preamble:i], self.input[i])
            if not res:
                print(f" Star 1 = {self.input[i]}")
                return self.input[i]
        return 0

    def star2(self):
        invalidNumber = self.star1()
        for i in range(len(self.input)):
            for j in range(len(self.input)):
                sumOfArray = sum(self.input[i:j])
                if invalidNumber == sumOfArray:
                    mini = min(self.input[i:j])
                    maxi = max(self.input[i:j])
                    res = mini + maxi
                    print(f" Star 2 = {res}")
                    return res

    def checkIfSumOfTail(self, tail, val):
        combined = [i+j for i in tail for j in tail]
        return val in combined
