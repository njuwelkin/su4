from individual import *
from candidates import *
from cipai import *

txt = AllPatterns[1]['sample']
lines = []
for line in txt.split('\n'):
    line = line.strip()
    if len(line) == 0:
        continue
    words = line.split('/')
    lines.append(words)

print(lines)

cp = CiPattern(AllPatterns[1])
wg = WordGenerator()
candidates = wg.getCandidates(['轻寒'], 8000)
indv = Individual(cp, candidates, '轻寒', lines)
print(indv)
print(indv.fitness())
print(indv.f_cache.fit_array)
