import random

"""
    'H': Wall
    'O': Bean
    ' ': Nothing
"""


class Map:
    wall = 'H'
    bean = 'O'
    nothing = ' '

    def __init__(self, *, max_x, max_y, bean_rate, wall_rate):
        self.max_x = max_x
        self.max_y = max_y
        self.bean_rate = bean_rate
        self.wall_rate = wall_rate
        self.inner_map = []
        self.build_map()

    def build_map(self):
        generate_map = []

        # generate outer walls
        for x in range(self.max_x + 2):
            generate_map.append([])

            if x == 0 or x == self.max_x + 1:
                for y in range(self.max_y + 2):
                    generate_map[x].append(self.wall)
            else:
                generate_map[x].append(self.wall)
                for y in range(self.max_y):
                    generate_map[x].append(self.nothing)
                generate_map[x].append(self.wall)

        # generate inner walls and beans
        for x in range(1, self.max_x + 1):
            for y in range(1, self.max_y + 1):
                if random.random() < self.wall_rate:
                    generate_map[x][y] = self.wall
                elif random.random() < self.bean_rate:
                    generate_map[x][y] = self.bean

        self.inner_map = generate_map

    def print_map(self):
        temp_list = []
        print("'%c': Wall, '%c': Bean, '%c': Nothing" % (self.wall, self.bean, self.nothing))
        print("↓y →x")
        for y in range(self.max_y + 2):
            for x in range(self.max_x + 2):
                temp_list.append(self.inner_map[x][y])
            print("".join(temp_list))
            temp_list.clear()
