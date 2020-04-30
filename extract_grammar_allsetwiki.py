from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\manik\Documents\chromedriver\chromedriver.exe")

save_file = open("export_hsk5.txt", "w", encoding="utf8")
wrong_link_file = open("link_with_wrong.txt", "w", encoding="utf8")


	#print(text , sep)

with open("allsetwiki_hsk5_link.txt", encoding="utf8") as f:
	for line in f:
	#for lk in range(0,1):
		url_short = line
		url = "https://resources.allsetlearning.com" + url_short

		#url = "https://resources.allsetlearning.com/chinese/grammar/Expressing_%22related_to...%22_with_%22you_guan_de%22"
		#time.sleep(3)
		driver.get(url)
		time.sleep(3)

		#jiegou = driver.find_element_by_xpath("/html/body/section/div[3]/div[4]/div[2]/div/div/div[2]/h1")
		
		jiegou = driver.find_elements_by_class_name("jiegou")

		usedfor = driver.find_element_by_xpath("//*[@id='ibox']/ul/li[6]/div[2]")

		heading = driver.find_element_by_xpath("//*[@id='innerbodycontent']/div/div[2]/h1")

		sen = driver.find_elements_by_class_name("spaced")

		wrong = driver.find_elements_by_class_name("x")

		# To find page containing wrong sentences, to be cleaned manually from text file
		found = False
		if len(wrong) > 0:
			found = True
			print("..............Found..............."+url)
			save_file.write("..............Found...............")
		#jiegou_str = " :: "
		
		for j in jiegou:
			print("\n.........................................................\n")
			jiegou_str = ":: " + j.text + " ::"
			print(jiegou_str)
			save_file.write(jiegou_str)
			print("\n.........................................................\n")
			#print(j.text)
			save_file.write("\n\n")

		#print(usedfor.text, heading.text)

		#for j in jiegou:
			#print(j.text)
		st_sen=""
		for s in sen:
			st_sen = str(s.text)
			if len(wrong) > 0 and wrong[0].text in st_sen:
				continue
				
			if "。" in st_sen or "." in st_sen:
				sep = "。"
				st_sen = st_sen.split(sep,1)[0].strip()
				st_sen += " " + sep
			if "？" in st_sen:
				sep = "？"
				st_sen = st_sen.split(sep,1)[0].strip()
				st_sen  += " " + sep
			
			# Page containing multiple grammar structures should be manually cleaned
			# For single grammar structure. It is simple
			all_set = st_sen +"\t"+ jiegou_str +"\t"+ usedfor.text +"\t"+ heading.text + "\t" + url
			
			print(all_set)
			save_file.write(all_set)
		print("\n\n")
		save_file.write("\n\n")
