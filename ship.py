import turtle

class Ship:
    def __init__(self, coords_x, coords_y, coords_ship, ungle, size):
        self.ungle = ungle
        self.size = size
        self.coords_ship = coords_ship
        self.coords_x = coords_x
        self.coords_y = coords_y
        self.coords_ship = self.ship_all_coords()
        #self.draw = self.PaintShip(self.cells)

    def ship_all_coords(self):
        if self.ungle == 90:
            coords_x = self.coords_ship[0]
            coords_y = self.coords_y[int(self.coords_ship[1])]
            return [coords_x, coords_y]


    class PaintShip:
        turtle.speed(1000)
        def __init__(self, coords):
            self.coords = coords
            self.ungle = ungle
            self.size = size
            self.ship_painter()

        def painting(self):
            turtle.penup()
            turtle.goto(self.coords[0], self.coords[1])
            turtle.pendown()

            for i in range(4):
                turtle.forward(20)
                turtle.right(90)
                i += 1
            turtle.left(90)

        def ship_painter(self):
            self.painting()



if __name__ == "__main__":
    answer = "y"
    ship1 = Ship(['a', 'b', 'c'], [1, 2, 3], 'b3', 90, 1)
    print(ship1.coords_ship)
    while answer is "y":
        turtle.penup()
        turtle.done()




