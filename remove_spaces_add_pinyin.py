import pinyin

save_file = open("hsk_sen_no_space.txt", "w", encoding="utf8")
add_pinyin = open("hsk1_pinyin.txt", "w", encoding="utf8")

with open("hsk1_only_sentences.txt", encoding="utf8") as f:
	for line in f:
		save_file.write(line.replace(" ",""))
		add_pinyin.write(pinyin.get(line))
		print(pinyin.get(line))
