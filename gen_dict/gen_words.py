from collections import OrderedDict
import sys

processed_lines = 330350

d = {}

f = open("./res/all_songci_cut.txt", "r")
for i in range(processed_lines):
    line = f.readline()
    words = line.split('/')
    for w in words:
        w = w.strip()
        if w in [',', '.', '$$$34567$$$'] or len(w) == 0:
            continue

        c_flag = False
        for c in w:
            if not ('\u4e00' <= c <= '\u9fa5'):
                c_flag = True
        if c_flag:
            continue

        if d.get(w) is None:
            d[w] = 1
        else:
            d[w] += 1

d = OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))

if len(sys.argv) == 1:
    l = 2
else:
    l = int(sys.argv[1])

if len(sys.argv) < 3:
    thr = 1
else:
    thr = int(sys.argv[2])

for k, v in d.items():
    if len(k) == l or (l == 3 and len(k) > l):
        if v >= thr:
            print(k, v)
