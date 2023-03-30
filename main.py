#import requests
#from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


#test
url = "https://www.ranker.com/list/best-kpop-maknae-members/ranker-music"
url2 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url3 = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"


us_ag = UserAgent()
user_agent = us_ag.random

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--disable-blink-features=AutomationControlled")

s = Service(
    executable_path="chromedriver.exe"
)

driver = webdriver.Chrome(
    service=s,
    options=options
)

try:
    i = 0
    driver.get(url=url)
    time.sleep(3)
    while i != 60:
        i = i + 1
        driver.execute_script("window.scrollBy(0,1000)", "")
        try:
            element = driver.find_element(By.XPATH, '//button[@class="button_main__b1K6d button_large__mns0w button_secondary__1ZG1U NextList_main__39AJ4"]')
            print(element)
            print("find elem")
            break
        except:
            print("Скролим страницу")

        time.sleep(1)
    time.sleep(2)
    with open("data.html", "w", encoding='utf-8') as file:
        file.write(driver.page_source)
    print("Страница скопирована")
    time.sleep(6)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

