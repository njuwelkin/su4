from loader import *

changes_str = """十 0
分 *
夕 0
和 *
歌 0
食 *
相 *
行 0
白 0
华 0
中 *
青 0
从 *
重 *
三 0
先 0
歌 0
夜 1
菲 0
别 0
长 *
独 0
闻 0
竹 0
霓 0
烛 *
横 *
衣 0
极 0
间 *
难 *
鲜 0
煎 0
菊 0"""

changes = changes_str.split('\n')
changes = [i.strip().split() for i in changes]
change_dict = {k: v for k, v in changes}

pz_dict = loadPZDict("./res/char_pz.txt")

for k, v in pz_dict.items():
    if change_dict.get(k) is None:
        print(k, v)
    else:
        print(k, change_dict[k])
