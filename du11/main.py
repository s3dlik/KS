from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.alza.cz")
driver.implicitly_wait(10)

search = driver.find_element(By.ID, 'edtSearch')
search.send_keys("Asus x515")
search.send_keys(Keys.RETURN)

driver.quit()