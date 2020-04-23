from bs4 import BeautifulSoup
import requests
#url = "https://resources.allsetlearning.com/chinese/grammar/HSK_1_grammar_points"
#url = "https://resources.allsetlearning.com/chinese/grammar/HSK_2_grammar_points"
#url = "https://resources.allsetlearning.com/chinese/grammar/HSK_3_grammar_points"
#url = "https://resources.allsetlearning.com/chinese/grammar/HSK_4_grammar_points"
#url = "https://resources.allsetlearning.com/chinese/grammar/HSK_5_grammar_points"
url = "https://resources.allsetlearning.com/chinese/grammar/HSK_6_grammar_points"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
tables = soup.findAll("table", {"class":"wikitable"})

def listToString(s):
	str1 = ""
	for ele in s:
		str1 += ele
	return str1

for t in tables:
	tr = t.findAll("tr")
	td = t.findAll("td")
	#tr[0].findAll("th")[0].contents
	#tr[0].findAll("th")[1].contents
	#tr[0].findAll("th")[2].contents
	#thead = tr[0].findAll("th")[0].contents + " , "+ tr[0].findAll("th")[1].contents +" , "+ tr[0].findAll("th")[2].contents
	#print(thead)
	for t in tr:
		try:
			link = t.findAll("td")[0].a.get("href")
			title = t.findAll("td")[0].a.get("title")
			article = t.findAll("td")[0].a.contents

			pattern = t.findAll("td")[1].contents

			example = t.findAll("td")[2].span.contents
			ex_st = ""
			for ex in example:
				ex1 = str(ex)
				#if ex.startswith('<') or ex.endswith('>'):
				ex1 = ex1.replace("<em>","")
				ex1 = ex1.replace("</em>","")
				ex1 = ex1.replace("<strong>","")
				ex1 = ex1.replace("</strong>","")
				ex1 = ex1.replace("<p>","")
				ex1 = ex1.replace("</p>","")
				ex1 = ex1.replace("/","")
				ex_st += ex1
			#print(ex_st)

			st = link + "	"+ title +  "	"+ listToString(article) +  "	"+ listToString(pattern) + "	" + str(ex_st)
			#print(type(link),type(title), type(article), type(pattern), type(example))
			#print(type(example))
			print(st)

		except Exception as e:
			#print(e)
			pass

