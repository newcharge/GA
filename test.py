from map import Map
from strategy import Strategy
from individual import Individual

# test_map = Map(max_x=10, max_y=10, bean_rate=0.5, wall_rate=0.8)
# test_map.print_map()

# test_strategy = Strategy()
# test_strategy.print_table()
# test_strategy.print_sim_table()
# test_another_strategy = Strategy(sim_code="123456000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
# test_another_strategy.print_sim_table()
# test_another_strategy.print_table()

# test_one = Individual(Strategy(sim_code="123456000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))
# print(test_one.get_sub_x())
# print(len(test_one.get_sub_x()))
# print(test_one.get_sub_y())
# print(len(test_one.get_sub_y()))
#
# from genetic import cal_adaptability
#
# print("test")
# individual = Individual(st=Strategy(sim_code="656" * 81))
# individual.st.print_table()
# li = []
# for i in range(1):
#     li.append(cal_adaptability(individual, 2))
#     individual.goal = 0
# individual.goal = sum(li) // len(li)
# print(individual.goal)
# print(individual.x)
# print(individual.y)
