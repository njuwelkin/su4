from relevancy import Relevancy
from su4_config import *
import numpy as np
from copy import deepcopy

class Individual(object):
    class FitnessCache(object):
        def __init__(this, owner, topic):
            this.owner = owner
            this.topic = topic
            this.r = Relevancy.getInstance()
            this.count_lines = np.zeros(len(owner.lines), dtype = 'uint32')

            this.fit_lines = np.zeros(len(owner.lines))
            this.fit_array = np.zeros((len(owner.lines), MAX_LINE_LEN))
            this.fitness = 0

            count = 0
            for i, line in enumerate(owner.lines):
                count_line = 0
                for j, w in enumerate(line):
                    count += 1
                    count_line += 1

                    this.fit_array[i, j] = W1 * this.r.get_relevancy(topic, w)
                    if j!= 0:
                        w0 = line[j - 1]
                        tmp = this.r.get_relevancy(w0, w)
                        this.fit_array[i, j - 1] += W2 * tmp / 2.0
                        this.fit_array[i, j] += W2 * tmp / 2.0

                this.count_lines[i] = count_line

            this.count_words = count
            this.fit_lines = this.fit_array.sum(1) / this.count_lines
            this.fitness = this.fit_array.sum() / count

            #print(count)
            #print(this.fit_lines)
            #print(this.fit_array)
            #print(this.fitness)

        def _calcFit(this, i, j):
            new_word = this.owner.lines[i][j]
            new_topic = this.r.get_relevancy(this.topic, new_word)
            r0 = r1 = 0
            if j != 0:
                r0 = this.r.get_relevancy(this.owner.lines[i][j-1], new_word)
            if j < this.count_lines[i] - 1:
                r1 = this.r.get_relevancy(new_word, this.owner.lines[i][j+1])

            newVal = W1 * new_topic + W2 * (r0 + r1) / 2.0
            return newVal

        def _update(this, i, j):
            newVal = this._calcFit(i, j)
            this.fit_array[i, j] = newVal

        def refresh(this):
            this.fit_lines = this.fit_array.sum(1) / this.count_lines
            this.fitness = this.fit_array.sum() / this.count_words

        def update(this, i, j, refresh = True):
            if j != 0:
                this._update(i, j-1)
            if j < this.count_lines[i] - 1:
                this._update(i, j+1)

            this._update(i, j)
            if refresh:
                this.refresh()

        def tryUpdate(this, i, j, refresh = True):
            new_word = this.owner.lines[i][j]
            oldVal = this.fit_array[i, j]

            newVal = this._calcFit(i, j)
            if newVal > oldVal:
                if j != 0:
                    this._update(i, j-1)
                if j < this.count_lines[i] - 1:
                    this._update(i, j+1)
                this.fit_array[i, j] = newVal
                if refresh:
                    this.refresh()
                return True

            return False

        def getFitForWord(this, i, j):
            return this.fit_array[i, j]

        def getMinFitWord(this):
            minval = 1.0
            for i in range(this.fit_array.shape[0]):
                for j in range(this.count_lines[i]):
                    val = this.fit_array[i, j]
                    if val == 0:
                        return (i, j)
                    if val < minval:
                        minval = val
                        x, y = i, j
            return (x, y)

        def getMinFitLine(this):
            return this.fit_lines.argmin()

    def __init__(self, pattern, candidates, topic, content=None):
        self.pattern = pattern
        self.candidates = candidates
        self.words = {}

        lines = []
        if content is None:
            for pline in pattern.lines:
                line = []
                for p in pline:
                    pz, pos, yun= p
                    line.append(self._get_random_word(pz, yun, pos))
                lines.append(line)
        else:
            for cline in content:
                line = []
                for word in cline:
                    line.append(word)
                lines.append(line)

        self.lines = lines
        self.f_cache = self.FitnessCache(self, topic)

    def update(self, i, j, word=None, refresh=True):
        if word is None:
            pz, pos, yun = self.pattern.lines[i][j]
            word = self._get_random_word(pz, yun, pos)
        self.lines[i][j] = word
        self.f_cache.update(i, j, refresh)

    def evolution(self, i, j):
        for l in range(1000):
            oldWord = self.lines[i][j]
            self.words[oldWord] = 0
            pz, pos, yun = self.pattern.lines[i][j]
            word = self._get_random_word(pz, yun, pos)
            self.lines[i][j] = word
            #print(self)
            print(i, j)
            print(self.f_cache.fit_array)
            if self.f_cache.tryUpdate(i, j):
                return True
        return False

    def _get_random_word(self, pz, yun, pos):
        while True:
            word = self.candidates.getRandomWord(pz, yun, pos)
            if self.words.get(word) is None or self.words[word] == 0:
                self.words[word] = 1
                return word

    def __str__(self):
        tmp=[''.join(l) for l in self.lines]
        return '\n'.join(tmp)

    def fitness(self):
        return self.f_cache.fitness

    def clone(self):
        return self.__class__(self.pattern, self.candidates, self.f_cache.topic, self.lines)

if __name__ == '__main__':
    from candidates import *
    from cipai import *
    cp = CiPattern(AllPatterns[0])
    wg = WordGenerator()
    candidates = wg.getCandidates(['周郎'], 8000)
    indv = Individual(cp, candidates, '周郎')
    print(indv.f_cache.getMinFitWord())
    print(indv.f_cache.getMinFitLine())
    print(indv.f_cache.fit_array)
    print(indv)
    indv2 = indv.clone()
    print(indv2.f_cache.fit_array)
    print(indv2)

