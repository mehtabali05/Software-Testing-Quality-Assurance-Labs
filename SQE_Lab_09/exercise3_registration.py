
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # Open DemoQA registration form
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")

    # First Name
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name.send_keys("Mehtab")

    # Last Name
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Ali")

    # Email
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("mehtab.test@example.com")

    # Select Male gender using its label
    male_label = driver.find_element(
        By.CSS_SELECTOR, "label[for='gender-radio-1']"
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        male_label
    )

    male_label.click()

    # Mobile Number (10 digits)
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("0300123456")

    # Verify entered values
    print("First Name:", first_name.get_attribute("value"))
    print("Last Name:", last_name.get_attribute("value"))
    print("Email:", email.get_attribute("value"))
    print("Mobile:", mobile.get_attribute("value"))

    # Verify gender selection
    male_radio = driver.find_element(By.ID, "gender-radio-1")
    print("Male Selected:", male_radio.is_selected())

finally:
    # Close browser
    driver.quit()
