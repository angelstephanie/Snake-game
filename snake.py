from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        new_body = Turtle("square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(position)
        self.body.append(new_body)

    def extend(self):
        self.add_body(self.body[-1].position())

    def move(self):
        for body_no in range(len(self.body) - 1, 0, -1):
            x_coordinate = self.body[body_no - 1].xcor()
            y_coordinate = self.body[body_no - 1].ycor()
            self.body[body_no].goto(x_coordinate, y_coordinate)
        self.head.fd(MOVE_DISTANCE)

    def reset(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
    # def head_on_body(self):
    #     for body in range(len(self.body)-1, 2,-1)
    #         if self.head.position() == body.position():
    #             return True

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)
