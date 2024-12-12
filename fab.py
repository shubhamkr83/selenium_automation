import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load sensitive data from environment variables
EMAIL = os.getenv('EMAIL', 'ishaan.sharma@thriwe.com')
PASSWORD = os.getenv('PASSWORD', 'Delhi@1234')

WEMAIL = "shubham@thriwe.com"
WPASSWORD = "Delhi@404"

# URLs
URLS = {
    "login": "https://smerewards.bankfab.com/login",
    "dashboard": "https://smerewards.bankfab.com/dashboard",
    "claim_history": "https://smerewards.bankfab.com/history",
    "profile": "https://smerewards.bankfab.com/profile",
    "contact": "https://smerewards.bankfab.com/contact"
}

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get(URLS['login'])
wait.until(EC.url_contains(URLS['login']))


def check_url(name, expected_url):
    # Check if the current URL matches the expected URL.
    wait.until(EC.url_contains(expected_url))
    current_url = driver.current_url
    if current_url == expected_url:
        print(f"{name} URL matched.")
    else:
        print(f"{name} URL did not match. Expected: {expected_url}, but got: {current_url}")


def login(email, password):
    # Perform login with the given email and password.

    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys(email)

    submit_button = driver.find_element(By.CLASS_NAME, 'PrimaryButton_button__pdJaq')
    submit_button.click()

    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys(password)
    submit_button.click()


def check_login_status():
    logout_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@class='PrimaryButton_button__pdJaq'][normalize-space()='Logout'])[2]"))
    )
    if "Logout" in logout_btn.text:
        print("Login Successful")
    else:
        print("Login Failed")


def check_alert(testcase_name, expected_message):
    # Check if the alert message matches the expected message.
    time.sleep(1.4)
    alert = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
    alert_msg = alert.text
    # print(alert_msg)
    if alert_msg == expected_message:
        print(f"{testcase_name} Test case passed")
    else:
        print(f"{testcase_name} Test case failed: Expected '{expected_message}', but got '{alert_msg}'")


def logout():
    """Perform logout and verify it."""
    logout_btn = driver.find_element(By.XPATH,
                                     "(//button[@class='PrimaryButton_button__pdJaq'][normalize-space()='Logout'])[2]")
    wait.until(EC.element_to_be_clickable(logout_btn)).click()
    wait.until(EC.url_contains(URLS['login']))

    if URLS['login'] in driver.current_url:
        print("Logout Successful")
    else:
        print("Logout Failed")
        print(f"Expected URL: {URLS['login']}, but got: {driver.current_url}")


def run_test_cases():
    """Run various login test cases."""

    # Wrong email and wrong password testcase
    login(WEMAIL, WPASSWORD)
    check_alert("Wrong email and wrong password", "Email/Password entered is incorrect. Please retry or try login via "
                                                  "OTP.")
    driver.refresh()

    # Wrong email and Correct Password testcase
    login(WEMAIL, PASSWORD)
    check_alert("Wrong email and Correct Password",
                "Email/Password entered is incorrect. Please retry or try login via OTP.")
    driver.refresh()

    # Correct email and Wrong password testcase
    login(EMAIL, WPASSWORD)
    check_alert("Correct email and Wrong password",
                "Email/Password entered is incorrect. Please retry or try login via OTP.")
    driver.refresh()

    # Blank email testcase
    driver.find_element(By.CLASS_NAME, 'PrimaryButton_button__pdJaq').click()
    check_alert("Blank email", "Please fill your registered email id to Login")
    driver.refresh()

    # Blank Password testcase
    login(EMAIL, "")
    check_alert("Correct email and Blank Password", "Please enter a password")
    driver.refresh()

    # Right email and password
    login(EMAIL, PASSWORD)
    check_login_status()


try:

    check_url("Login url", URLS['login'])

    run_test_cases()

    # Check navigation to various URLs after login
    driver.find_element(By.LINK_TEXT, "My Benefits").click()
    check_url("Dashboard", URLS['dashboard'])

    driver.find_element(By.LINK_TEXT, "Claimed Benefits").click()
    check_url("Claim history", URLS['claim_history'])

    driver.find_element(By.LINK_TEXT, "Profile").click()
    check_url("Profile", URLS['profile'])

    driver.find_element(By.LINK_TEXT, "Contact").click()
    check_url("Contact", URLS['contact'])

    # Perform logout and check
    logout()

finally:
    driver.quit()
