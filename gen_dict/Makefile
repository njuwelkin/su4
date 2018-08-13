all: ../su4/res/words_pzy.txt ../su4/res/w_w.npy.npz ../su4/res/words_pos.txt
	echo "Done"

# copy to su4 work folder
../su4/res/w_w.npy.npz: output/w_w.npy.npz
	cp output/w_w.npy.npz ../su4/res/

../su4/res/words_pzy.txt: output/words_pzy.txt
	cp output/words_pzy.txt ../su4/res/

../su4/res/sim.npy.npz: output/sim.npy.npz
	cp output/sim.npy.npz ../su4/res/

../su4/res/words_pos.txt: output/words_pos.txt
	cp output/words_pos.txt ../su4/res/

# merge pos
output/words_pos.txt: res/words_pos.txt output/words_freq.txt
	python merge_pos_dict.py > output/words_pos.txt

# sim matrix
output/sim.npy.npz:sim_matrix.py output/words_freq.txt res/all_songci_cut.txt
	python sim_matrix.py

# merge w_w matrix
output/w_w.npy.npz: merge_matrix.py output/w_w1.npy.npz output/w_w2.npy.npz output/w_w3.npy.npz
	python merge_matrix.py

# word to word matrix
output/w_w1.npy.npz: calc_cos.py output/w_c.npy.npz
	python calc_cos.py ./output/w_c.npy.npz ./output/w_w1.npy

output/w_w2.npy.npz: calc_cos.py output/w_c2.npy.npz
	python calc_cos.py ./output/w_c2.npy.npz ./output/w_w2.npy

output/w_w3.npy.npz: calc_cos.py output/w_c3.npy.npz
	python calc_cos.py ./output/w_c3.npy.npz ./output/w_w3.npy

# word to ci matrix
output/w_c.npy.npz: matrix.py output/words_pzy.txt res/all_songci_raw.txt
	python matrix.py

output/w_c2.npy.npz: matrix2.py output/words_pzy.txt res/all_songci_cut.txt
	python matrix2.py

output/w_c3.npy.npz: matrix3.py output/words_pzy.txt res/all_songci_cut.txt
	python matrix3.py

# P Z Y for each word
output/words_pzy.txt: gen_pzy_dict.py output/char_yun.txt output/char_pz_new.txt output/words_freq.txt
	python gen_pzy_dict.py > output/words_pzy.txt

# Ping Ze for each char
output/char_pz_new.txt: old2new.py res/char_pz.txt
	python old2new.py > output/char_pz_new.txt

# Pinyin for each char
output/char_yun.txt: gen_category_pinyin.py res/pinyin.txt
	python gen_category_pinyin.py > output/char_yun.txt

# All words with frequency
output/words_freq.txt: output/words_2.txt output/words_3.txt output/words_1.txt
	cat output/words_2.txt > output/words_freq.txt
	cat output/words_3.txt >> output/words_freq.txt
	cat output/words_1.txt >> output/words_freq.txt

output/words_2.txt: gen_words.py res/all_songci_cut.txt
	python gen_words.py 2 5 > output/words_2.txt

output/words_3.txt: gen_words.py res/all_songci_cut.txt
	python gen_words.py 3 2 > output/words_3.txt

output/words_1.txt: gen_words.py res/all_songci_cut.txt
	python gen_words.py 1 3 > output/words_1.txt

clean:
	rm output/*

