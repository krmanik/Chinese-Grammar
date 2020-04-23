#https://stackoverflow.com/questions/61205124/how-to-get-different-data-from-same-class-in-selenium-python

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\manik\Documents\chromedriver\chromedriver.exe")

save_file = open("export_hsk3.txt", "w", encoding="utf8")
with open("allsetwiki_hsk3_link.txt", encoding="utf8") as f:
		#for line in f:
		for lk in range(0,1):

			#url_short = line
			#url = "https://resources.allsetlearning.com" + url_short
			url = "https://resources.allsetlearning.com/chinese/grammar/Reduplication_of_adjectives"
			time.sleep(1)
			driver.get(url)
			#structureelements = WebDriverWait(driver,15).until(EC.visibility_of_all_elements_located((By.XPATH,"//h3[./span[text()='Structure']]/following::div[1]")))
			structureelements = WebDriverWait(driver,15).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"jiegou")))

			for structure in structureelements:
				print("============================")
				print(structure.text)
				save_file.write(structure.text)
				print("========================================")

				
				#for example in structure.find_elements_by_xpath(".//following::h3[1]/following::div[1]//li[@class='spaced']"):
				for example in structure.find_elements_by_xpath("//div[@class='jiegou']/p[1]|//li[@class='spaced']"):
					print(example.text)
					save_file.write(example.text)
					
