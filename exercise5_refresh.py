
from selenium import webdriver
import time

# Start Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://www.python.org")

# Store title before refresh
title_before = driver.title
print("Title Before Refresh:", title_before)

time.sleep(2)

# Refresh website
driver.refresh()
time.sleep(2)

# Store title after refresh
title_after = driver.title
print("Title After Refresh:", title_after)

# Compare both titles
if title_before == title_after:
    print("Result: Title remained the same.")
else:
    print("Result: Title changed.")

# Close browser
driver.quit()
