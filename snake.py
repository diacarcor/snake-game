from turtle import Turtle

STARTING_X_COORDINATES = (0, -20, -40)
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coordinate in STARTING_X_COORDINATES:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(coordinate)
            self.segments.append(segment)

    def move(self):
        snake_segments = self.segments
        for segment_index in range(len(snake_segments) - 1, 0, -1):
            new_x_cor = snake_segments[segment_index - 1].xcor()
            new_y_cor = snake_segments[segment_index - 1].ycor()
            snake_segments[segment_index].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(DOWN)
