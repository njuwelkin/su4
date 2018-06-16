all: output/words_pzy.txt
	echo "Done"

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
	python gen_words.py 1 5 > output/words_1.txt

clean:
	rm output/*