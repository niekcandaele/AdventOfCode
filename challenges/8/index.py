import re


class Challenge():
    accumulator = 0
    currentOp = 0

    def __init__(self, data):
        self.input = data.splitlines()
        self.accumulator = 0
        self.currentOp = 0

    def star1(self):
        return self.executeInstructions(self.input)

    def star2(self):
        permutations = self.createPermutations()
        for perm in permutations:
            try:
                #print(f'Executing {perm}')
                res = self.executeInstructions(perm)
            except IndexError as e:
                print(f'Fully ran through, accumulator = {self.accumulator}')
                return self.accumulator

    def executeOp(self, op):
        opType = op[:3]
        opAmount = re.findall(r'[-+]\d+', op)[0]
        #print(f"Beep boop, executing {opType} {opAmount}")

        if opType == 'acc':
            self.accumulator += int(opAmount)

        if opType == 'jmp':
            self.currentOp += int(opAmount)
            # We dont want to increment currentOp for jmp instruction
            return

        self.currentOp += 1

    def createPermutations(self):
        permutations = []
        i = 0
        for op in self.input:

            if op.startswith('jmp') or op.startswith('nop'):
                copy = self.input.copy()
                if op.startswith('jmp'):
                    copy[i] = re.sub(r'(jmp)', 'nop', op)
                if op.startswith('nop'):
                    copy[i] = re.sub(r'(nop)', 'jmp', op)
                permutations.append(copy)

            i += 1

        print(
            f"Generated {len(permutations)} permutations of original instructions")
        return permutations

    def executeInstructions(self, instructions):
        self.accumulator = 0
        self.currentOp = 0
        executedOps = []
        exit = False
        while exit != True:
            if self.currentOp in executedOps:
                #print(f'Already executed {self.currentOp} - {executedOps}')
                return self.accumulator

            executedOps.append(self.currentOp)
            self.executeOp(instructions[self.currentOp])
            pass
