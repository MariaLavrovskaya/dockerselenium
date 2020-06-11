import comments
import os
from selenium import webdriver
import comments
import selenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

browser = comments.setUp()

print(os.getenv('BROWSER', 'chrome'))
#Driver code for extracting comments using Chrome


links1 = []
with open('main/file2.csv', newline='') as f:
    reader = csv.reader(f)
    links = list(reader)[1:]
    for division in links:
        for link in division:
            links1.append(link)
    print(links1)
not_sorted_comments1 = comments.extract_comments(links1, 'C4VMK')
print(not_sorted_comments1)
comcom = pd.DataFrame(data={"col1": not_sorted_comments1})
comcom.to_csv("./comments.csv", sep=',', index=False)



#Personal comments
#instagram_page, xpath_to_links, xpath_to_comments = comments.taking_input()
#links = comments.extract_links(instagram_page, xpath_to_links)
#unique_links = comments.unique_links(links)
#comments.data_storing(unique_links)


