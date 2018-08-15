from population import *
from roulette_wheel_selection import *
from uniform_crossover import *

if __name__ == '__main__':
    p = Population(QUANTITY, '周郎')
    print(p.all_fits())
    print(p.bestIndv())
    print(p.bestIndv().fitness())

    selection = RouletteWheelSelection()
    #print(selection.select(p)[0])
    #print(selection.select(p)[1])

    crossover = UniformCrossover(0.8, 0.2, 0.5)

    for gen in range(100):
        best_indv = p.bestIndv().clone()
        print(gen)
        #print(p.all_fits())
        print("    max:", best_indv.fitness())
        print("    min:", p.worstFit())
        #print(best_indv)

        indvs=[]
        local_size = p.size // 2
        for _ in range(local_size):
            parents = selection.select(p)
            children = crossover.cross(*parents)
            indvs.extend(children)

        indvs[0] = best_indv
        p.indvs = indvs

    print(best_indv)
    print(best_indv.f_cache.fit_array)
