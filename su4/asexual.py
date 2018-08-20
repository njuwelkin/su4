from individual import *

from candidates import *
from cipai import *

import random
import sys


def main(topic):
    cp = CiPattern(AllPatterns[1])
    wg = WordGenerator()
    cand = wg.getCandidates([topic], 18000)
    indv = Individual(cp, cand, topic)

    count = 0
    for l in range(1000):
        if random.random() > 0.5:
            i, j = indv.f_cache.getMinFitWord()
            if not indv.evolution(i, j):
                j1 = j - 1
                while j1 >= 0 and not indv.evolution(i, j1):
                    j1 -= 1

                j2 = j + 1
                while j2 < indv.f_cache.count_lines[i] and not indv.evolution(i, j2):
                    j2 += 1

                if j1 < 0 and j2 >= indv.f_cache.count_lines[i]:
                    count += 1
            else:
                count = 0
        else:
            i = random.randint(0, len(indv.lines) - 1)
            j = random.randint(0, indv.f_cache.count_lines[i] - 1)
            indv.evolution(i, j)

        if count > 30:
            break
        #print(indv.fitness())
    print(topic)
    print(indv)
    print(indv.fitness(), '\n')
    #print(indv.f_cache.fit_array)

if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        topic = sys.argv[i]
        main(topic)

