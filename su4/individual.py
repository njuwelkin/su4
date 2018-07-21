
class Individual(object):
    def __init__(self, pattern, candidates):
        self.pattern = pattern
        self.candidates = candidates
        self.words = {}
        lines = []

        for pline in pattern.lines:
            line = []
            for p in pline:
                pz, pos, yun= p
                line.append(self._get_random_word(pz, yun, pos))
            lines.append(line)

        self.lines = lines

    def _get_random_word(self, pz, yun, pos):
        while True:
            word = candidates.getRandomWord(pz, yun, pos)
            if self.words.get(word) is None:
                self.words[word] = 1
            return word
        

    def __str__(self):
        tmp=[''.join(l) for l in self.lines]
        return '\n'.join(tmp)

if __name__ == '__main__':
    from candidates import *
    from cipai import *
    cp = CiPattern(fqyb, fqyb_grammar)
    wg = WordGenerator()
    candidates = wg.getCandidates(['龄'], 8000)
    indv = Individual(cp, candidates)
    print(indv)
