import re
import collections


class Challenge():
    def __init__(self, data):
        self.input = self.parseInput(data)
        print(self.input)

    def star1(self):
        invalids = []

        for ticketToCheck in self.input[1]:
            for numberToCheck in ticketToCheck.split(','):
                if not self.checkRules(numberToCheck, self.input[0]):
                    invalids.append(int(numberToCheck))
                

        return sum(invalids)

    def star2(self):
        rulesWithName = self.input[2]

        valids = []

        for ticketToCheck in self.input[1]:
            valid = True
            for numberToCheck in ticketToCheck.split(','):
                if not self.checkRules(numberToCheck, self.input[0]):
                    print('Not valid!')
                    valid = False
            if valid:
                valids.append(ticketToCheck.split(','))
                

        print(f'Valid tickets = {valids}')
        print(f'Check with rules = {rulesWithName}')

        possible = collections.defaultdict(set)
        for index in range(len(rulesWithName)):
            for field, scope in rulesWithName.items():
                print(field, scope)
                if all(self.checkScope(ticket[index], scope) for ticket in valids):
                    possible[field].add(index)
            
        print(f'Possible = {possible}')

        my_ticket = [97,101,149,103,137,61,59,223,263,179,131,113,241,127,53,109,89,173,107,211]
        departures = 1
        official = dict()
        for field in sorted(possible, key=lambda i: len(possible[i])):
            for index in possible[field]:
                if index not in official.values():
                    official[field] = index
                    print(field)
                    if 'depart' in field:
                        departures = departures * my_ticket[index]
        return departures

    def checkRules(self, num, rules):
        valid = False
        for rule in rules:
            #print(f'Checking {num} vs {rule}')
            minMaxPre = re.findall(r'\d+', rule[0])
            minMaxAfter = re.findall(r'\d+', rule[1])
            num = int(num)
            if num >= int(minMaxPre[0]) and num <= int(minMaxPre[1]) or num >= int(minMaxAfter[0]) and num <= int(minMaxAfter[1]):
                valid = True
        return valid
            

    def checkScope(self, num, rule):
        valid = False
        print(f'Checking {num} vs {rule}')
        minMaxPre = re.findall(r'\d+', rule[0])
        minMaxAfter = re.findall(r'\d+', rule[1])
        num = int(num)
        if num >= int(minMaxPre[0]) and num <= int(minMaxPre[1]) or num >= int(minMaxAfter[0]) and num <= int(minMaxAfter[1]):
            valid = True
        return valid

    def parseInput(self,data):
        rules = []
        rulesWithName = {}
        preRules = re.findall(r'.+: \d+-\d+ or \d+-\d+', data)
        print(f' Prerules = {preRules}')
        for rule in preRules:
            print(rule)
            type = re.findall(r'(.+):', rule)[0]
            print(type)
            ruleNumbers = re.findall(r'\d+-\d+ or \d+-\d+', rule)[0]
            a = ruleNumbers.split(' or ')
            rules.append(a)
            rulesWithName[type] = a
        
        splitdata = data.splitlines()
        ticketsToCheckIdx = splitdata.index('nearby tickets:')
        ticketsToCheck = splitdata[ticketsToCheckIdx+1:]

        return [rules, ticketsToCheck, rulesWithName]
        