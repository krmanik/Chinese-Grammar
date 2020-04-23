from gtts import gTTS
# name:audio - hsk1_grammar_sent1.mp3

# Change file name
with open("hsk1_only_sentences.txt", encoding="utf8") as f:
	i = 1
	for line in f:
		tts = gTTS(line, lang="zh-cn")
		name = "hsk1_grammar_sent"+ str(i) +".mp3"
		i += 1
		tts.save(name)
