import loader

pzy_dict = loader.loadFreqFile('output/words_freq.txt')
pos_dict = loader.loadPosDict('res/words_pos.txt')

for w, f in pzy_dict.items():
    s = w + " " + f
    if pos_dict.get(w):
        l = pos_dict[w]
        if len(l) > 1:
            s += " " + " ".join(l[1:])
    print(s)
