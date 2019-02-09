from strategy import Strategy
from map import Map
import random


class Individual:
    # generate a individual with a strategy table
    def __init__(self, *, st=Strategy()):
        self.x = 1
        self.y = 1
        self.goal = 0
        self.st = st

    @staticmethod
    def read_map(bean_map, x, y):
        if bean_map[x][y] == Map.nothing:
            return "nothing"
        elif bean_map[x][y] == Map.wall:
            return "wall"
        elif bean_map[x][y] == Map.bean:
            return "bean"

    def movement(self, *, bean_map):
        x = self.x
        y = self.y
        north_state = self.read_map(bean_map, x, y - 1)
        east_state = self.read_map(bean_map, x + 1, y)
        south_state = self.read_map(bean_map, x, y + 1)
        west_state = self.read_map(bean_map, x - 1, y)
        current_state = self.read_map(bean_map, x, y)
        strategy = self.st.strategy_table[north_state][east_state][south_state][west_state][current_state]

        if Strategy.base_strategy[strategy] == 'auto':
            num_list = [0, 1, 2, 3]
            state_list = [north_state, east_state, south_state, west_state]
            while state_list:
                rand_num = random.randint(0, len(state_list) - 1)
                if state_list[rand_num] != Map.wall:
                    strategy = num_list[rand_num]
                    break
                else:
                    num_list.pop(rand_num)
                    state_list.pop(rand_num)

        if Strategy.base_strategy[strategy] == 'north' and north_state != 'wall':
            self.y -= 1
        elif Strategy.base_strategy[strategy] == 'north' and north_state == 'wall':
            self.goal -= 5
        elif Strategy.base_strategy[strategy] == 'east' and east_state != 'wall':
            self.x += 1
        elif Strategy.base_strategy[strategy] == 'east' and east_state == 'wall':
            self.goal -= 5
        elif Strategy.base_strategy[strategy] == 'south' and south_state != 'wall':
            self.y += 1
        elif Strategy.base_strategy[strategy] == 'south' and south_state == 'wall':
            self.goal -= 5
        elif Strategy.base_strategy[strategy] == 'west' and west_state != 'wall':
            self.x -= 1
        elif Strategy.base_strategy[strategy] == 'west' and west_state == 'wall':
            self.goal -= 5

        if Strategy.base_strategy[strategy] == 'eat' and current_state == 'bean':
            self.goal += 10
            bean_map[x][y] = Map.nothing
        elif Strategy.base_strategy[strategy] == 'eat' and current_state != 'bean':
            self.goal -= 1

    def get_sub_x(self):
        sim_code = self.st.get_sim_code()
        return sim_code[0:121]

    def get_sub_y(self):
        sim_code = self.st.get_sim_code()
        return sim_code[121:243]
