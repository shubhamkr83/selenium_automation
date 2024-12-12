import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load sensitive data from environment variables
EMAIL = os.getenv('EMAIL', 'Priyanka.malik@thriwe.com')
PASSWORD = os.getenv('PASSWORD', 'Welcome@1122')

# Wrong Email ID and password
WEMAIL = 'shubham@thriwe.com'
IEMAIL = 'shubham.thriwe.com'
WPASSWORD = 'Wrong@500'

# URLs
login_url = "https://cbdgolf.thriwe.com/login"
dashboard_url = "https://cbdgolf.thriwe.com/dashboard"
offer_url = "https://cbdgolf.thriwe.com/offer-details"
manage_booking_url = "https://cbdgolf.thriwe.com/manage-bookings"
profile_url = "https://cbdgolf.thriwe.com/profile"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Open the website with the form
driver.get(login_url)

# Check if the login URL is correct
if login_url in driver.current_url:
    print("Login URL matched")
else:
    print("Login URL did not match")
    print(f"Expected URL: {login_url}, but got: {driver.current_url}")


# Function to re-locate elements
def locate_elements():
    global email_field, password_field, submit_button
    email_field = driver.find_element(By.NAME, 'email')
    password_field = driver.find_element(By.NAME, 'password')
    submit_button = driver.find_element(By.CSS_SELECTOR,
                                        "button[class='btn border-2 rounded-pill btn-purple px-4 p-2']")


# ---------------------Login----------------------
# Wrong email and Correct Password testcase
driver.refresh()
locate_elements()
email_field.send_keys(WEMAIL)
password_field.send_keys(PASSWORD)
time.sleep(20)
submit_button.click()
alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
alert_msg = alert.text
if alert_msg == "Invalid Username or Password.":
    print("Wrong email testcase checked")
else:
    print("Wrong email testcase failed")

# Right email and Wrong password testcase
driver.refresh()
locate_elements()
email_field.send_keys(EMAIL)
password_field.send_keys(WPASSWORD)
time.sleep(20)
submit_button.click()
alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
alert_msg = alert.text
if alert_msg == "Invalid Username or Password.":
    print("Wrong password testcase checked")
else:
    print("Wrong password testcase failed")

# Wrong email and password testcase
driver.refresh()
locate_elements()
email_field.send_keys(WEMAIL)
password_field.send_keys(WPASSWORD)
time.sleep(20)
submit_button.click()
alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
alert_msg = alert.text
if alert_msg == "Invalid Username or Password.":
    print("Wrong email and password testcase checked")
else:
    print("Wrong email and password testcase failed")

# Blank email and password testcase
driver.refresh()
locate_elements()
submit_button.click()
blank_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter valid email')]")))
blank_password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a password')]")))

# Check if both elements are displayed
if blank_email.is_displayed() and blank_password.is_displayed():
    blank_email_msg = blank_email.text
    blank_password_msg = blank_password.text
    # Validate the messages
    if blank_email_msg == "Please enter valid email" and blank_password_msg == "Please enter a password":
        print("Blank email and password testcase checked")
    else:
        print("Blank email and password testcase failed")

# Invalid email and wrong password
driver.refresh()
locate_elements()
email_field.send_keys(IEMAIL)
password_field.send_keys(WPASSWORD)
submit_button.click()
blank_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter valid email')]")))
if blank_email.is_displayed():
    blank_email_msg = blank_email.text
    # Validate the messages
    if blank_email_msg == "Please enter valid email":
        print("Invalid email testcase checked")
    else:
        print("Invalid email testcase not displayed")

# Positive case
driver.refresh()
locate_elements()
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
time.sleep(20)
submit_button.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "clicktoproceed"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            "div[class='modal-footer'] button[class='btn border-2 "
                                                            "rounded-pill btn-purple px-4 p-2']"))).click()
profile = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@id='navbarScrollingDropdown']")))
profile_text = profile.text
if profile.is_displayed():
    print("Login Successful")
else:
    print("Login Failed")

# ------------------Header Locators----------------
Offer_btn = driver.find_element(By.LINK_TEXT, "Offer Details")
Manage_Booking_btn = driver.find_element(By.LINK_TEXT, "Manage Bookings")
Profile_btn = driver.find_element(By.LINK_TEXT, "Manage Profile")


# -----------------Url Check-----------------------
def check_url(name, expected_url):
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url))
    current_url = driver.current_url
    if expected_url in current_url:
        print(f"{name} URL matched")
    else:
        print(f"{name} URL did not match. Expected URL: {expected_url}, got: {current_url}")


# Booking url check
check_url("Dashboard", dashboard_url)

# Offer url check
Offer_btn.click()
check_url("Booking", offer_url)

# Manage_Booking url check
Manage_Booking_btn.click()
check_url("Terms", manage_booking_url)

# Profile url check
Profile_btn.click()
check_url("FAQ", profile_url)

# --------------------Logout----------------------
profile.click()
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
WebDriverWait(driver, 10).until(EC.url_contains(login_url))
if login_url in driver.current_url:
    print("Logout Successful")
else:
    print("Logout Failed")

# Close the driver
driver.quit()
