def _isChinese(c):
    X,Y = ['\u4e00','\u9fa5']
    return (X <= c <= Y)

def loadPinyinDict(path):
    f = open(path, "r")
    d = {}
    for line in f.readlines():
        l = line.strip()
        k = l[0]
        assert(_isChinese(k))
        if d.get(k) is None:
            d[k] = set()
        ps = l[1:].split()
        for i in ps:
            d[k].add(i)
    f.close()
    return d


def loadFreqFile(path):
    return _loadKeyValue(path)

def loadYunDict(path):
    return _loadKeyValues(path)

def loadPZDict(path):
    return _loadKeyValue(path)

def loadPZYDict(path):
    return _loadKeyValues(path)

def _loadKeyValue(path):
    f = open(path, "r")
    d = {}
    for line in f.readlines():
        l = line.strip().split()
        assert(len(l) == 2)
        d[l[0]] = l[1]
    f.close()
    return d

def _loadKeyValues(path):
    f = open(path, "r")
    d = {}
    for line in f.readlines():
        l = line.strip().split()
        d[l[0]] = l[1:]
    f.close()
    return d


