
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open Wikipedia
    driver.get("https://www.wikipedia.org/")

    # Find all anchor elements
    links = driver.find_elements(By.TAG_NAME, "a")

    # Print total links
    print("Total Links on Wikipedia:", len(links))

finally:
    # Close browser
    driver.quit()
