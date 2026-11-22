
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Locate search field
    search = driver.find_element(By.NAME, "q")

    # Type first query
    search.send_keys("Selenium WebDriver tutorial")
    time.sleep(1)

    # Clear search field
    search.clear()

    # Type second query
    search.send_keys("Software Quality Engineering")

    # Press Enter
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    # Print page title
    print("Results page title:", driver.title)

finally:
    # Close browser
    driver.quit()
