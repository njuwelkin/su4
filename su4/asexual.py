from individual import *

from candidates import *
from cipai import *

import random
import sys


def main(topic, pid):
    cp = CiPattern(AllPatterns[pid])
    wg = WordGenerator()
    cand = wg.getCandidates([topic], 18000)
    indv = Individual(cp, cand, topic)

    for l in range(1000):
        if random.random() > 0.5:
            i, j = indv.f_cache.getMinFitWord()
            if not indv.evolution(i, j):
                updated = False
                i = j = 0
                while not updated and i < indv.totalLines():
                    while not updated and j < indv.lineLen(i):
                        if indv.evolution(i, j):
                            print(i, j)
                            updated = True
                        j += 1
                    i += 1
                if not updated:
                    break
        else:
            i = random.randint(0, len(indv.lines) - 1)
            j = random.randint(0, indv.f_cache.count_lines[i] - 1)
            indv.evolution(i, j)

        print(indv.fitness())
    print(topic)
    print(indv)
    print(indv.fitness(), '\n')
    print(indv.f_cache.fit_array)

if __name__ == '__main__':
    topic = sys.argv[1]
    pid = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    main(topic, pid)

