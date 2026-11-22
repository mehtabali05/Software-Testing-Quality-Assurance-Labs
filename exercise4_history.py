
from selenium import webdriver
import time

# Start Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open three websites
driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://www.wikipedia.org")
time.sleep(2)

driver.get("https://www.python.org")
time.sleep(2)

# Go Back twice
driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

print("Title After Going Back Twice:", driver.title)

# Go Forward once
driver.forward()
time.sleep(2)

print("Title After Going Forward Once:", driver.title)

# Close browser
driver.quit()
