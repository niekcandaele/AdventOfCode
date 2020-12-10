from functools import lru_cache

class Challenge():
    def __init__(self, data):
        self.input = list(map(lambda x: int(x), data.splitlines()))
        self.input.sort()
        # Add our device to the input list
        self.input.append(max(self.input) + 3)
        # Add the outlet
        self.input.insert(0,0)
        print(self.input)

    def star1(self):
        diffs = self.calcJumps(self.input)
        return diffs.count(1) * (diffs.count(3)) 

    def star2(self):
        perms = self.calcPerms(max(self.input))
        return perms
                
    def calcJumps(self, list):
        return [list[n]-list[n-1] for n in range(1,len(list))]

    # ngl, saw this 'lru_cache' on the subreddit and dont fully understand it
    # But with this decorator, function goes fast :)
    # See: https://docs.python.org/3/library/functools.html#functools.lru_cache
    @lru_cache
    def calcPerms(self, x):
        """
        Start at highest (your device) (= x)

        if recursionEndCondition() ( => x == 0 because that's the start of the list)
            return
        else 
            loop over acceptable jumps
            if x - jump is in the chain, we should also calc all the paths to this value
                total += recurse(x - 1)
                return total
        """

        if x == 0:
            return 1
        else:
            subTotal = 0
            # Acceptable differences are 1,2 and 3
            for i in range(1, 4):
                if x-i in self.input: 
                    subTotal += self.calcPerms(x-i)
            return subTotal
