from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.visionplus.id/movies")

link = driver.find_elements(By.XPATH, "//div[@class='img-wrapper-ratio ra-3-2']/div")
link_list = []
for i in link:
    link_img = i.find_element(By.TAG_NAME, 'img').get_attribute('src')
    print(link_img)
