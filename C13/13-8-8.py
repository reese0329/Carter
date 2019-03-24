class Ball:
    def __int__(self,color,size,direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction =="down":
            self.direction = "up"

myBall = Ball("red","small","down")
print("I just created a ball.")
print("My ball is",myBall.size)
print("My ball is",myBall.color)
print("My ball's direction is ",myBall.direction)
print
myBall.bounce()