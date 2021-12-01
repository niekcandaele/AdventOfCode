class Challenge():
    def __init__(self, data):
        self.input = data.split('\n')

    def star1(self):
        count = 1
        i = 0
        for line in self.input:
            if self.input[i - 1] < self.input[i]:
                count += 1
            i += 1
        return count

    def star2(self):
        windows = []

        for i in range(2, len(self.input)):
            windows.append([int(i) for i in self.input[i - 2:i + 1]])
            

        sum_of_windows = []
        for window in windows:
            sum_of_windows.append(sum(window))
        
        count = 0
        i = 0
        for line in sum_of_windows:
            if sum_of_windows[i - 1] < sum_of_windows[i]:
                count += 1
            i += 1
        print(count)            
        return count
