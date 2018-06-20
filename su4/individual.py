
class Individual(object):
    def __init__(self, pattern, candidates):
        self.pattern = pattern
        self.candidates = candidates
        self.words = {}
        lines = []

        for pline in pattern.lines:
            line = []
            for i in range(len(pline[0]) - 1):
                pz = pline[0][i]
                line.append(candidates.getRandomWord(pz))
            pz = pline[0][i+1]
            word = self._get_random_word(pz, pline[1])
            line.append(word)
            lines.append(line)

        self.lines = lines

    def _get_random_word(self, pz, yun):
        while True:
            word = candidates.getRandomWord(pz, yun)
            if self.words.get(word) is None:
                self.words[word] = 1
            return word
        

    def __str__(self):
        tmp=[''.join(l) for l in self.lines]
        return '\n'.join(tmp)

if __name__ == '__main__':
    from candidates import *
    from cipai import *
    cp = CiPattern(qpy1)
    wg = WordGenerator()
    candidates = wg.getCandidates(['周郎'], 2000)
    indv = Individual(cp, candidates)
    print(indv)
