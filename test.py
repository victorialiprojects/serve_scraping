from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Replace 'path/to/geckodriver' with the actual path to your geckodriver executable
driver_path = '/Users/victoriali/SERVESCRAPING/geckodriver'
driver = webdriver.Firefox()

# Open a webpage
url = 'https://warrior.uwaterloo.ca/'
driver.get(url)

time.sleep(5)

another_button_selector = 'div.col:nth-child(16) > a:nth-child(1) > span:nth-child(1) > img:nth-child(1)'  # Replace with the actual CSS selector of the button
another_button = driver.find_element(By.CSS_SELECTOR, another_button_selector)
another_button.click()
time.sleep(2)

second_button_selector = 'li.page-item:nth-child(5) > a:nth-child(1)'
second_button = driver.find_element(By.CSS_SELECTOR, second_button_selector)
second_button.click()
time.sleep(2)

button_selector = '#gdpr-cookie-accept'
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))

# Click the button
button.click()

serve = 'div.program-list-item:nth-child(52) > a:nth-child(1) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)'
element2 = driver.find_element(By.CSS_SELECTOR, serve)
element2.click()
time.sleep(2)

# Find button by text content
button_text = 'Fri'
button_xpath = f"//button[.//span[@class='single-date-select-button-day' and text()='{button_text}']]"
button = driver.find_element(By.XPATH, button_xpath)
# Scroll the button into view using JavaScript
driver.execute_script("arguments[0].scrollIntoView(true);", button)

time.sleep(2)
button.click()


driver.close()