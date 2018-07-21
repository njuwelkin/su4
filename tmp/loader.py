

def loadKeyValue(path, f=None):
    f = open(path, "r")
    d = {}
    for line in f.readlines():
        l = line.strip().split()
        assert(len(l) == 2)
        d[l[0]] = l[1]
    f.close()
    return d

def loadKeyValues(path):
    f = open(path, "r")
    d = {}
    for line in f.readlines():
        l = line.strip().split()
        d[l[0]] = l[1:]
    f.close()
    return d

if __name__ == '__main__':
    print(loadAllCutSongci("./res/all_songci_cut.txt"))
