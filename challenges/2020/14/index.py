import os;

class Challenge():
    def __init__(self, data):
        self.input = data

    def star1(self):
        return 'aaa'

    def star2(self):
        return 'aaa'


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

smallinput = open(os.path.join(__location__, 'smallinput.txt')).read()
input = open(os.path.join(__location__, 'input.txt')).read()

if __name__ == '__main__':

    print(f'Star 1 is {Challenge(smallinput).star1()}')
    print(f'Star 2 is {Challenge(smallinput).star2()}')