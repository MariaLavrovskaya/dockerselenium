from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


global links
global allcomments
#global browser

def setUp():
    #global browser
    caps = {'browserName': os.getenv('BROWSER', 'chrome')}
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=caps
    )
    return browser

def extract_links(instagram_page, xpath_to_links):
    links = []
    scheight = .1
    posts = []
    #browser = webdriver.Chrome('/Users/maria/desktop/chromedriver')
    browser = setUp()
    browser.get(f"{instagram_page}")
    #finding the links by scrolling the page down
    while scheight < 9.9:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight += .01
        posts = browser.find_elements_by_xpath(f"//div[@class='{xpath_to_links}']")
        for elem in posts[:40]:
            try:
                WebDriverWait(elem, 80).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href]")))
                WebDriverWait(elem, 40).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href]")))
                print(elem.find_element_by_css_selector('a').get_attribute('href'), len(links))
                links.append(elem.find_element_by_css_selector('a').get_attribute('href'))
            except TimeoutException:
                continue
            except StaleElementReferenceException:
                continue
            if len(links) == 100:
                break
        if len(links) == 100:
            break
    browser.quit()
    return set(links)


#Since the scrolling function returns the links that have duplicates, we need to create list of the set
def unique_links(links):
    unique_links = [link for link in links]
    return unique_links


#Extracting comments for each post
def extract_comments(links, xpath_to_comments):
    not_sorted_comments = []
    browser = setUp()
    for link in links:
        browser.get(link)
        allcomments = browser.find_elements_by_xpath(f"//div[@class='{xpath_to_comments}']")
        for comment in allcomments:
            not_sorted_comments += comment.text.split('Ответить')
    browser.quit()
    return not_sorted_comments

def data_storing(unique_links):
    df = pd.DataFrame(data={"col1": unique_links})
    return df.to_csv("./file.csv", sep=',',index=False)



