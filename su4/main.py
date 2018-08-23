from population import *
from roulette_wheel_selection import *
from uniform_crossover import *
from mutation import *

import sys

def main(topic, pid):
    p = Population(QUANTITY, topic, AllPatterns[pid])

    selection = RouletteWheelSelection()

    crossover = UniformCrossover(0.7, 0.1, 0.3)
    mutation = Mutation(0.5)

    for gen in range(500):
        best_indv = p.bestIndv().clone()
        print(gen)
        #print(p.all_fits())
        print("    max:", best_indv.fitness())
        print("    min:", p.worstFit())
        print(best_indv)

        indvs=[]
        local_size = p.size // 2
        for _ in range(local_size):
            parents = selection.select(p)
            children = crossover.cross(*parents)
            children = [mutation.mutate(child) for child in children]
            indvs.extend(children)

        indvs[0] = best_indv
        p.indvs = indvs

    print("\n\n%s-%s" % (AllPatterns[pid]['name'], topic))
    print(best_indv)
    print(best_indv.fitness())
    print(best_indv.f_cache.fit_array)

if __name__ == '__main__':
    topic = sys.argv[1]
    pid = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    main(topic, pid)
