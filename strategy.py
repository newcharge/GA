"""
    north/east/south/west: move to north
    stay: do nothing
    eat: eat the bean
    auto: move to a random direction
"""


class Strategy:
    states = {"wall", "bean", "nothing"}
    base_strategy = {0: 'north', 1: 'east', 2: 'south', 3: 'west', 4: 'stay', 5: 'eat', 6: 'auto'}

    def __init__(self, *, sim_code="default"):
        if sim_code == "default":
            self.strategy_table = self.create_table()
        else:
            self.strategy_table = self.decode_as_table(sim_code=sim_code)

    # create a strategy table, with state north/east/south/west/current
    def create_table(self):
        states = self.states
        generate_table = {}
        for north_state in states:
            generate_table[north_state] = {}
            for east_state in states:
                generate_table[north_state][east_state] = {}
                for south_state in states:
                    generate_table[north_state][east_state][south_state] = {}
                    for west_state in states:
                        generate_table[north_state][east_state][south_state][west_state] = {}
                        for current_state in states:
                            generate_table[north_state][east_state][south_state][west_state][current_state] = 0
        return generate_table

    def print_table(self):
        print("strategy table:")
        print("north    east     south    west     current  strategy ")
        states = self.states
        for north_state in states:
            for east_state in states:
                for south_state in states:
                    for west_state in states:
                        for current_state in states:
                            print("%-9s%-9s%-9s%-9s%-9s" % (north_state,
                                                            east_state,
                                                            south_state,
                                                            west_state,
                                                            current_state),
                                  end='')
                            num = self.strategy_table[north_state][east_state][south_state][west_state][current_state]
                            print("%-9s" % (self.base_strategy[num]),
                                  end='')
                            print("")

    def get_sim_code(self):
        strategy_list = []
        states = self.states
        for north_state in states:
            for east_state in states:
                for south_state in states:
                    for west_state in states:
                        for current_state in states:
                            num = self.strategy_table[north_state][east_state][south_state][west_state][current_state]
                            strategy_list.append(str(num))
        return "".join(strategy_list)

    def print_sim_table(self):
        print("strategy table:", "".join(self.get_sim_code()))

    def decode_as_table(self, *, sim_code):
        num_list = list(map(int, list(sim_code)))
        states = self.states
        generate_table = {}
        for north_state in states:
            generate_table[north_state] = {}
            for east_state in states:
                generate_table[north_state][east_state] = {}
                for south_state in states:
                    generate_table[north_state][east_state][south_state] = {}
                    for west_state in states:
                        generate_table[north_state][east_state][south_state][west_state] = {}
                        for current_state in states:
                            generate_table[north_state][east_state][south_state][west_state][current_state]\
                                = num_list.pop(0)
        return generate_table
