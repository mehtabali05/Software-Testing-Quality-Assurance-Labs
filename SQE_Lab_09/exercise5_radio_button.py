
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # Open registration form
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")

    # Locate radio inputs
    male_radio = driver.find_element(
        By.ID, "gender-radio-1"
    )

    female_radio = driver.find_element(
        By.ID, "gender-radio-2"
    )

    # Locate labels
    male_label = driver.find_element(
        By.CSS_SELECTOR, "label[for='gender-radio-1']"
    )

    female_label = driver.find_element(
        By.CSS_SELECTOR, "label[for='gender-radio-2']"
    )

    # Select Male
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        male_label
    )

    male_label.click()

    print("Male Selected:", male_radio.is_selected())
    print("Female Selected:", female_radio.is_selected())

    # Select Female
    female_label.click()

    print("\nAfter Selecting Female:")

    print("Male Selected:", male_radio.is_selected())
    print("Female Selected:", female_radio.is_selected())

finally:
    # Close browser
    driver.quit()
