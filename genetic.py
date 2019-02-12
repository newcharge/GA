from individual import Individual
from strategy import Strategy
from map import Map
import random

exec_time = 100
action_time = 200
mutation_prob = 0.005
gene_size = 243
evo_time = 1000
# 以下参数不可随意更改了
group_size = 200
p_size = 200 - 70


def cal_adaptability(individual, act_time):
    sup_map = Map(max_x=10, max_y=10, bean_rate=0.5, wall_rate=0)
    # sup_map.print_map()
    bean_map = sup_map.inner_map
    for act_num in range(act_time):
        individual.movement(bean_map=bean_map)
    return individual.goal


def genetic_algorithm(bef_group):
    # 执行任务并计算适应度
    for individual in bef_group:
        goal_list = []
        for exec_num in range(exec_time):
            goal_list.append(cal_adaptability(individual, action_time))
            individual.goal = 0
        adaptability = sum(goal_list) // len(goal_list)
        individual.goal = adaptability
        # print("one's goal:", individual.goal)
    bef_group.sort(key=lambda x: x.goal, reverse=True)

    sample = list(map(lambda x: x.goal, bef_group))
    print(sample)
    print("均值：", sum(sample) // len(sample), "最大值：", max(sample), "最小值", min(sample))

    # 进化
    selector = []
    next_group = []
    for group_i in range(group_size):
        for curr_num in range(max([group_size - group_i - p_size, 1])):
            selector.append(group_i)

    # print(selector)

    while len(next_group) < group_size:
        father = random.randint(0, len(selector) - 1)
        mother = random.randint(0, len(selector) - 1)
        father = selector[father]
        mother = selector[mother]
        if father == mother:
            continue
        else:
            cut_p = random.randint(1, gene_size - 1)
            f_x = bef_group[father].get_sub_x(cut_p)
            f_y = bef_group[father].get_sub_y(cut_p)
            m_x = bef_group[mother].get_sub_x(cut_p)
            m_y = bef_group[mother].get_sub_y(cut_p)
            new_bro = f_x + m_y
            new_sis = m_x + f_y
            # 变异
            while random.random() < mutation_prob:
                gene_i = random.randint(0, gene_size - 1)
                random_num = random.randint(0, 6)
                while random_num == new_bro[gene_i]:
                    random_num = random.randint(0, 6)
                new_bro_list = list(new_bro)
                new_bro_list[gene_i] = str(random_num)
                new_bro = "".join(new_bro_list)

            while random.random() < mutation_prob:
                gene_i = random.randint(0, gene_size - 1)
                random_num = random.randint(0, 6)
                while random_num == new_sis[gene_i]:
                    random_num = random.randint(0, 6)
                new_sis_list = list(new_sis)
                new_sis_list[gene_i] = str(random_num)
                new_sis = "".join(new_sis_list)

            next_group.append(Individual(st=Strategy(sim_code=new_bro)))
            next_group.append(Individual(st=Strategy(sim_code=new_sis)))
    return next_group


# 生成初始群体
group = []
for group_index in range(group_size):
    # 生成随机代码
    gene_list = []
    for gene_index in range(gene_size):
        gene_list.append(str(random.randint(0, 6)))
    sim_code = "".join(gene_list)
    group.append(Individual(st=Strategy(sim_code=sim_code)))

for evo_num in range(evo_time):
    print("evolution----------", evo_num)
    group = genetic_algorithm(group)

for ele in group:
    gl = []
    for i in range(exec_time):
        b_map = Map(max_x=10, max_y=10, bean_rate=0.5, wall_rate=0).inner_map
        for j in range(action_time):
            ele.movement(bean_map=b_map)
        gl.append(ele.goal)
        ele.goal = 0
    ans = sum(gl) // len(gl)
    ele.goal = ans
    # print("one's goal:", individual.goal)
group.sort(key=lambda x: x.goal, reverse=True)
print("1:", group[0].goal)
group[0].st.print_table()
print("2:", group[1].goal)
group[1].st.print_sim_table()
