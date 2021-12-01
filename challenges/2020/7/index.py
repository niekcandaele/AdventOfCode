import re

f = open("./challenges/7/input.txt", "r")
input = f.read().splitlines()

rules = {}

# Parse the input into a usable dictionary
for rule in input:
    split = rule.split(' bags contain ')
    rules[split[0]] = {}

    contains = split[1:]
    containers = re.findall(r'\d [a-z ]+(?= bag)', contains[0])
    for container in containers:
        containerColour = re.findall(r'[^\d][a-z ]+', container)
        containerAmount = re.findall(r'\d', container)[0]
        rules[split[0]][containerColour[0].strip()] = containerAmount
        pass


print(rules)

# Recursively find the correct bags


def findBags(outerBag, trail):
    if 'shiny gold' in rules[outerBag]:
        return True
    else:
        for innerBag in rules[outerBag]:
            if innerBag not in trail:
                trail.append(innerBag)
                if findBags(innerBag, trail):
                    return True
        return False


def countBags(outer):
    count = 0
    if len(rules[outer]):
        for inner in rules[outer]:
            count += int(rules[outer][inner])
            count += int(rules[outer][inner]) * countBags(inner)
        return count
    else:
        return 0


amount = 0
for rule in rules:
    if findBags(rule, []):
        amount += 1

print(f"Part 1 = {amount}")
print(f"Part 2 = {countBags('shiny gold')}")
