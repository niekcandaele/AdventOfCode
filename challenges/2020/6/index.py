f = open("./challenges/6/input.txt", "r")
input = f.read().splitlines()

# hackerman
input.append('')

groups = []
currGroup = set()

for line in input:
    if line == '':
        groups.append(currGroup)
        currGroup = set()
    else:
        currGroup.add(line)


# --- part1

res = 0
for group in groups:
    persons = []

    for person in group:
        persons.append(set(person))

    res += len(set.union(*persons))
print(f"Part 1 {res}")


# ------- part2

res = 0
for group in groups:
    persons = []

    for person in group:
        persons.append(set(person))

    res += len(set.intersection(*persons))

print(f"Part 2 {res}")
