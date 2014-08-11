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
query_num = input()
d = Dice(numbers)

while query_num > 0:
    query_num -= 1
    top, front = map(int, raw_input().split())

    for x in xrange(3):
        if d.top() == top: break
        d.move_north()
        for x in xrange(3):
            if d.top() == top: break
            d.move_east()
    for x in xrange(3):
        if d.front() == front: break
        d.spin()

    print d.right()
            

    


        
