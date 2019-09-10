import map

# settings
player_map_start = [-350, 300]
computer_map_start = [-100, 300]

class Game:

    def __init__(self):
        self.player_pole = map.Pole(player_map_start)
        self.computer_pole = map.Pole(computer_map_start)


