import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

# Load sensitive data from environment variables
EMAIL = os.getenv('EMAIL', 'chhatra.pal@thriwe.com')
PASSWORD = os.getenv('PASSWORD', 'Test@1234')

WEMAIL = "shubham@thriwe.com"
WPASSWORD = "Delhi@404"

IEMAIL = "shubham.com"

# URLs
URLS = {
    "login": "https://emiratesnbdbenefits.thriwe.com/login",
    "dashboard": "https://emiratesnbdbenefits.thriwe.com/dashboard",
    "booking_history": "https://emiratesnbdbenefits.thriwe.com/booking-history",
    "terms": "https://emiratesnbdbenefits.thriwe.com/terms-and-conditions",
    "faq": "https://emiratesnbdbenefits.thriwe.com/faqs",
    "contact": "https://emiratesnbdbenefits.thriwe.com/contact"
}

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

def url_and_page_check(name, expected_url):
    wait.until(EC.url_contains(expected_url))
    current_url = driver.current_url
    bread_title = driver.find_element(By.CSS_SELECTOR, "div[class='bread-title'] h2").text
    if current_url == expected_url and bread_title == name:
        print(f"{name} URL matched and page load successfully")
    else:
        print(f"{name} URL did not match. Expected: {expected_url}, but got: {current_url}")

def login(email, password):
    # Perform login with the given email and password.
    email_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.ID, 'register_btn')

    email_field.send_keys(email)
    password_field.send_keys(password)

    time.sleep(10)

    submit_button.click()


def check_login_status():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='text-decoration-none custom-btn theme-2']"))
    ).click()

    profile = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "basic-nav-dropdown"))
    )

    if profile.is_displayed():
        print("Login Successful")
    else:
        print("Login Failed")


def check_alert(testcase_name, expected_message):
        alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='login_form_error']")))
        alert_msg = alert.text
        if alert_msg == expected_message:
            print(f"{testcase_name} Test case passed")
        else:
            print(f"{testcase_name} Test case failed: Expected '{expected_message}', but got '{alert_msg}'")
    
        


def logout():
    """Perform logout and verify it."""
    profile = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "basic-nav-dropdown"))
    )
    profile.click()
    logout_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'navItemCustom dropdown-item')]"))
    )
    logout_btn.click()

    WebDriverWait(driver, 10).until(EC.url_contains(URLS['login']))

    if URLS['login'] in driver.current_url:
        print("Logout Successful")
    else:
        print("Logout Failed")
        print(f"Expected URL: {URLS['login']}, but got: {driver.current_url}")



def run_test_cases():
    """Run various login test cases."""

    # Wrong email and wrong password testcase
    login(WEMAIL, WPASSWORD)
    check_alert("Wrong email and wrong password", "Invalid Username or Password.")
    driver.refresh()

    # Wrong email and Correct Password testcase
    login(WEMAIL, PASSWORD)
    check_alert("Wrong email and Correct Password", "Invalid Username or Password.")
    driver.refresh()

    # Correct email and Wrong password testcase
    login(EMAIL, WPASSWORD)
    check_alert("Correct email and Wrong password", "Invalid Username or Password.")
    driver.refresh()

    # Blank email and blank password testcase
    login("", "")
    email_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='login_email-error']"))).text
    password_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='password-error']"))).text
    if email_error == "Please enter an email" and password_error == "Please enter a password":
        print("Blank email and blank password testcase passed")
    driver.refresh()

    # Invalid email testcase
    login(IEMAIL, "")
    email_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='login_email-error']"))).text
    if email_error == "Please enter a valid email": 
        print("Invalid email testcase passed")
    driver.refresh()

    # Right email and password
    login(EMAIL, PASSWORD)
    check_login_status()


try:

    # Perform login check
    check_url("Login url", URLS['login'])

    # Perform login test cases
    run_test_cases()

    # Add time delay for 4 seconds
    time.sleep(3)

    # Perform booking history
    booking_history_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Booking History']")
    booking_history_btn.click()
    url_and_page_check("Booking History", URLS['booking_history'])
    
    # Add time delay for 4 seconds
    time.sleep(4)

    # Perform T&C and check
    driver.find_element(By.LINK_TEXT, "T&C").click()
    url_and_page_check("Terms And Conditions", URLS['terms'])
      

    # Perform FAQs and check
    driver.find_element(By.LINK_TEXT, "FAQs").click()
    url_and_page_check("Frequently Asked Questions", URLS['faq'])
    

    # Perform Contact Us and check
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    url_and_page_check("Contact Customer Support", URLS['contact'])
    

    # Perform logout and check
    logout()

finally:
    driver.quit()
