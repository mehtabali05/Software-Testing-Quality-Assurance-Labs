
from selenium import webdriver
import time

# Start Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Website 1
driver.get("https://www.google.com")
print("Website 1:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Website 2
driver.get("https://www.wikipedia.org")
print("Website 2:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Website 3
driver.get("https://www.python.org")
print("Website 3:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Go Back twice
driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

print("After Back Twice:", driver.title)

# Go Forward once
driver.forward()
time.sleep(2)

print("After Forward:", driver.title)

# Close Chrome
driver.quit()
