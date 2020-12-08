import re
f = open("./challenges/8/input.txt", "r")
input = f.read().splitlines()

print(input)

accumulator = 0
currentOp = 0


def executeOp(op):
    global accumulator
    global currentOp
    opType = op[:3]
    opAmount = re.findall(r'[-+]\d+', op)[0]
    #print(f"Beep boop, executing {opType} {opAmount}")

    if opType == 'acc':
        accumulator += int(opAmount)

    if opType == 'jmp':
        currentOp += int(opAmount)
        # We dont want to increment currentOp for jmp instruction
        return

    currentOp += 1


exit = True


permutations = []
i = 0
for op in input:

    if op.startswith('jmp') or op.startswith('nop'):
        copy = input.copy()
        if op.startswith('jmp'):
            copy[i] = re.sub(r'(jmp)', 'nop', op)
        if op.startswith('nop'):
            copy[i] = re.sub(r'(nop)', 'jmp', op)
        permutations.append(copy)

    i += 1

print(f"Generated {len(permutations)} permutations of original instructions")


def executeInstructions(instructions):
    global accumulator
    global currentOp
    accumulator = 0
    currentOp = 0
    executedOps = []
    exit = False
    while exit != True:
        if currentOp in executedOps:
            #print(f'Already executed {currentOp} - {executedOps}')
            return accumulator

        executedOps.append(currentOp)
        executeOp(instructions[currentOp])
        pass


for perm in permutations:
    try:
        #print(f'Executing {perm}')
        res = executeInstructions(perm)
    except IndexError as e:
        print(str(e))
        print(f'Fully ran through, accumulator = {accumulator}')
        pass

# 1 = 1553
# 2 = 1877


def star1(input):
    print('yay')
    pass


def star2(input):
    pass
