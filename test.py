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

# test_one = Individual(st=Strategy(sim_code="123456000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))
# print(test_one.get_sub_x(242))
# print(len(test_one.get_sub_x(242)))
# print(test_one.get_sub_y(242))
# print(len(test_one.get_sub_y(242)))
#
# from genetic import cal_adaptability
#
# print("test")
# individual = Individual(st=Strategy(sim_code="500500500500500500500500500500500500500500500500500500500500500500500500500500500511511511511511511511511511522522522533564533533522522522522522533511511533511511511511511511511511511511511522522522533500500533566566522522522533566566533566566"))
# individual.st.print_table()
# li = []
# for i in range(10000):
#     li.append(cal_adaptability(individual, 200))
#     individual.goal = 0
# li.sort(reverse=True)
# individual.goal = sum(li) // len(li)
# print(li)
# print(individual.goal)
# print(individual.x)
# print(individual.y)
