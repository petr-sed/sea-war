import turtle

class Ship:
    def __init__(self, coords_ship, ungle, size):
        self.ungle = ungle
        self.size = size
        self.coords_ship = coords_ship
        self.coords_ship = self.ship_all_coords()

    def ship_all_coords(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        if self.ungle == 90:
            x = self.coords_ship[0]
            y = []
            for i in range(self.size):
                z = int(self.coords_ship[1:]) + i
                y.append(z)
            coords_ship = [x, y]
            return coords_ship
        if self.ungle == 0:
            y = int(self.coords_ship[1:])
            ind = letters.index(self.coords_ship[0])
            x = []
            for i in range(self.size):
                x.append(letters[ind])
                ind += 1
            coords_ship = [x, y]
            return coords_ship

class ZoneAround:
    def __init__(self, coords_ship):
        self.coords_ship = coords_ship
        self.zone_around = self.ship_zone_around()

    def ship_zone_around(self):
        x = self.coords_ship[0]
        yy = self.coords_ship[1]
        k = yy
        k.append(2)
        return k

if __name__ == "__main__":
    answer = "y"
    ship1 = Ship('c3', 90, 2)
    print(ship1.coords_ship)
    print(ship1.zone_around)





