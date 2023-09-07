from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.visionplus.id/movies")

genre = driver.find_elements(By.CSS_SELECTOR, '.title-container')
movie_list = []
for i in genre:
    category = i.find_element(By.TAG_NAME, 'h2').text
    dt = {
        'Genre Film': category
    }
    movie_list.append(dt)

title = driver.find_elements(By.XPATH, "//div[@class='swiper-slide swiper-slide-list']")
title_list = []
for i in title:
    poster = i.find_element(By.TAG_NAME, 'img').get_attribute('alt').replace("poster ", "")
    dt = {
        'Title Film': poster
    }
    title_list.append(dt)

link = driver.find_elements(By.XPATH, "//div[@class='img-wrapper-ratio ra-3-2']/div")
link_list = []
for i in link:
    link_img = i.find_element(By.TAG_NAME, 'img').get_attribute('src')
    dt = {
        'Image': link_img
    }
    link_list.append(dt)


# Create pandas DataFrames
movie_df = pd.DataFrame(movie_list)
title_df = pd.DataFrame(title_list)
image_df = pd.DataFrame(link_list)

# Concatenate the DataFrames
combined_df = pd.concat([movie_df, title_df, image_df], axis=1)
combined_df.to_csv('assignment2test.csv')
driver.close()

