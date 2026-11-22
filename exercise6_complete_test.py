
from selenium import webdriver
import time

# Start Chrome
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open first website
driver.get("https://www.google.com")
print("First Website Title:", driver.title)
print("First Website URL:", driver.current_url)
time.sleep(2)

# Open second website
driver.get("https://www.wikipedia.org")
print("Second Website Title:", driver.title)
print("Second Website URL:", driver.current_url)
time.sleep(2)

# Go Back
driver.back()
time.sleep(2)
print("After Back:", driver.title)

# Go Forward
driver.forward()
time.sleep(2)
print("After Forward:", driver.title)

# Refresh page
driver.refresh()
time.sleep(2)
print("After Refresh:", driver.title)

# Close browser
driver.quit()
