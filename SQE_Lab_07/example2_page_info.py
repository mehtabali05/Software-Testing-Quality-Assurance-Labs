
from selenium import webdriver
import time

# Start Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open Python website
driver.get("https://www.python.org")

# Print website information
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

# Wait for 3 seconds so you can observe Chrome
time.sleep(3)

# Close browser
driver.quit()
