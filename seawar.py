import turtle
import math
import ship
answer = "y"
map_color = "black"
player_map_start = [-350, 300]
computer_map_start = [-100, 300]
turtle.speed(2000)



class Pole:
    ships = 10
    def __init__(self, coords):
        self.coords = coords
        self.map_painter()

    def border_paint(self):
        turtle.penup()
        turtle.goto(self.coords[0], self.coords[1])
        turtle.pendown()
        for i in range(4):
            turtle.forward(200)
            turtle.right(90)
            i += 1
        turtle.left(90)

    def vertical_lines(self):
        turtle.penup()
        turtle.goto(self.coords[0], self.coords[1])
        for i in range(9):
            if i % 2 != 1:
                self.coords[0] = self.coords[0] + 20
                turtle.goto(self.coords[0], self.coords[1])
                turtle.right(180)
                turtle.pendown()
                turtle.forward(200)
                turtle.penup()
            else:
                self.coords[0] = self.coords[0] + 20
                low_point = self.coords[1] - 200
                turtle.goto(self.coords[0], low_point)
                turtle.right(180)
                turtle.pendown()
                turtle.forward(200)
                turtle.penup()
        self.coords[0] = self.coords[0] - 180
        turtle.pendown()

    def horizontal_lines(self):
        turtle.penup()
        turtle.goto(self.coords[0], self.coords[1])
        turtle.right(90)
        for i in range(9):
            if i % 2 != 1:
                self.coords[1] = self.coords[1] - 20
                turtle.goto(self.coords[0], self.coords[1])
                turtle.right(180)
                turtle.pendown()
                turtle.forward(200)
                turtle.penup()
            else:
                self.coords[1] = self.coords[1] - 20
                left_point = self.coords[0] + 200
                turtle.goto(left_point, self.coords[1])
                turtle.right(180)
                turtle.pendown()
                turtle.forward(200)
                turtle.penup()
        self.coords[1] = self.coords[1] + 180
        turtle.pendown()

    def numbers(self):
        turtle.penup()

        for i in range(10):
            if i!=9:
                turtle.goto(self.coords[0] + (i * 20 + 7), self.coords[1] + 1)
            else:
                turtle.goto(self.coords[0] + (i * 20 + 3), self.coords[1] + 1)
            turtle.write(i + 1, font=("Arial", 10, "normal"))
            i+=1

    def letters(self):
        l=""
        for i in range(10):
            if i == 0:
                l = "a"
            elif i==1:
                l = "b"
            elif i == 2:
                l = "c"
            elif i == 3:
                l = "d"
            elif i == 4:
                l = "e"
            elif i == 5:
                l = "f"
            elif i == 6:
                l = "g"
            elif i == 7:
                l = "h"
            elif i == 8:
                l = "i"
            elif i == 9:
                l = "j"
            turtle.goto(self.coords[0] - 9, self.coords[1] - (i * 20 + 17))
            turtle.write(l, font=("Arial", 10, "normal"))
            i += 1



    def map_painter(self):
        self.border_paint()
        self.vertical_lines()
        self.horizontal_lines()
        self.numbers()
        self.letters()

while answer is "y":
    pole_player = Pole(player_map_start)
    pole_computer = Pole(computer_map_start)
    turtle.goto(player_map_start)
    player_ships = Ship(3, -320, 280, 90)

    turtle.done()


