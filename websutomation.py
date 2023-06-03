from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "D:\SPIT\chrome driver\chromedriver_win32"

service =  Service(executable_path=path)
driver = webdriver.Chrome(service = service)
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
df_headlines.to_csv('headline.csv')
pd.read_csv('headline.csv')

driver.quit()

