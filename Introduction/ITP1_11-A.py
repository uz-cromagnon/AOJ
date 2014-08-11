class Dice:
    def __init__(self, face):
        self.face = face
    def top(self):
        return self.face[0]
    def bottom(self):
        return self.face[5]
    def right(self):
        return self.face[2]
    def left(self):
        return self.face[3]
    def front(self):
        return self.face[1]
    def back(self):
        return self.face[4]
        
    def move_east(self):
        tmp = self.face[2]
        self.face[2] = self.face[0]
        self.face[0] = self.face[3]
        self.face[3] = self.face[5]
        self.face[5] = tmp
    def move_west(self):
        tmp = self.face[3]
        self.face[3] = self.face[0]
        self.face[0] = self.face[2]
        self.face[2] = self.face[5]
        self.face[5] = tmp
    def move_south(self):
        tmp = self.face[1]
        self.face[1] = self.face[0]
        self.face[0] = self.face[4]
        self.face[4] = self.face[5]
        self.face[5] = tmp
    def move_north(self):
        tmp = self.face[4]
        self.face[4] = self.face[0]
        self.face[0] = self.face[1]
        self.face[1] = self.face[5]
        self.face[5] = tmp
    def spin(self):
        tmp = self.face[3]
        self.face[3] = self.face[1]
        self.face[1] = self.face[2]
        self.face[2] = self.face[4]
        self.face[4] = tmp
    
numbers = map(int, raw_input().split())
if len(numbers) != 6: exit()
for x in numbers:
    if x < 0 or x > 100:
        exit()

d = Dice(numbers)
s = raw_input()
for c in s:
    if   c == 'E': d.move_east()
    elif c == 'W': d.move_west()
    elif c == 'S': d.move_south()
    elif c == 'N': d.move_north()
    else         : pass

print d.top()

        
