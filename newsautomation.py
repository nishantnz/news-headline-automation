from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service  import Service
import pandas as pd
from datetime import datetime
import os
import sys

#get the path of the executable that we are going to create
application_path = os.path.dirname(sys.executable)

now = datetime.now()

# convert time into string
#MMDDYYYY
month_day_year =now.strftime("%m%d%y")

website = "https://www.thesun.co.uk/sport/football/"
path = "D:\SPIT\chrome driver\chromedriver_win32"

#headless-mode

options = Options()
options.headless = True

service =  Service(executable_path=path)
driver = webdriver.Chrome(service = service,options=options)
driver.get(website)

#//div[@class="teaser__copy-container"]
 
titles = []
subtitles = []
links = []

containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')
for container in containers:
    title = container.find_element(by="xpath", value='./a/h3').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

df_headlines = pd.DataFrame({'title':titles,'subtitle':subtitles,'link':links})
df_headlines.to_csv(f'headline-{month_day_year}.csv')

driver.quit()

