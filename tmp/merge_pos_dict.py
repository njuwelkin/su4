import loader

pzy_dict = loader.loadKeyValue('../gen_dict/output/words_freq.txt')
pos_dict = loader.loadKeyValues('../su4/res/words_freq.txt')

for w, f in pzy_dict.items():
    s = w + " " + f
    if pos_dict.get(w):
        l = pos_dict[w]
        if len(l) > 1:
            s += " " + " ".join(l[1:])
    print(s)
