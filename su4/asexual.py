from individual import *

from candidates import *
from cipai import *

import random

cp = CiPattern(AllPatterns[0])
wg = WordGenerator()
cand = wg.getCandidates(['周郎'], 8000)
indv = Individual(cp, cand, '周郎')
print(indv.f_cache.getMinFitWord())
print(indv.f_cache.getMinFitLine())
print(indv)


for l in range(1000):
    print("*************")
    if random.random() > 0.5:
        i, j = indv.f_cache.getMinFitWord()
    else:
        i = random.randint(0, len(indv.lines) - 1)
        j = random.randint(0, indv.f_cache.count_lines[i] - 1)
    if not indv.evolution(i, j):
        break
print(indv)
