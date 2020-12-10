from functools import lru_cache

class Challenge():
    def __init__(self, data):
        self.input = list(map(lambda x: int(x), data.splitlines()))
        self.chain = [0]
        self.currentAdapter = 0
        print(self.input)

    def star1(self):
        for i in range(len(self.input)):
            self.getAdapter()
        print(self.chain)
        # Add our device to the end of the chain, which is always + 3
        self.chain.append(self.chain[len(self.chain) - 1] + 3)
        diffs = self.calcJumps(self.chain)
        print(f'Found {len(diffs)} diffs! With {diffs.count(1)} of 1 and {diffs.count(3)} of 3 {diffs}')

        answer = diffs.count(1) * (diffs.count(3))
        print(f'Finished! Answer is {answer}')
        return answer 

    def star2(self):
        for i in range(len(self.input)):
            self.getAdapter()
        # Add our device to the end of the chain, which is always + 3
        self.chain.append(self.chain[len(self.chain) - 1] + 3)

        perms = self.calcPerms(max(self.chain))
        return perms

    def getAdapter(self):
        for i in range(4):
            try:
                self.input.remove(self.currentAdapter + i)
                self.chain.append(self.currentAdapter + i)
                self.currentAdapter += i
                return self.currentAdapter + i
            except ValueError as err:
                pass
                
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
                if x-i in self.chain: 
                    subTotal += self.calcPerms(x-i)
            return subTotal
