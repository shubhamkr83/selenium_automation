import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from email_otp import Otp

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
URL = "https://axismagnusbenefits.thriwe.com/login"
driver.get(URL)
driver.maximize_window()


# Enter mobile number and login
driver.find_element(By.XPATH, "//input[@id='mobile']").send_keys("9650430195")
driver.find_element(By.XPATH, "//button[normalize-space()='Send OTP']").click()


# Wait for the OTP to arrive and be extracted
time.sleep(5)
username = "automationdib@gmail.com"
password = "ozwg ptkc xcnq koqk"
imap_server = "imap.gmail.com"
otp = Otp(username, password, imap_server).extract_otp_from_email()

# Input the OTP
c = 1
if otp is not None:
    for ele in range(0, len(otp)):
        if c != 6:
            driver.find_element(By.XPATH, f"(//input[@aria-label='Please enter OTP character 1'])[{c}]").click()
            driver.find_element(By.XPATH, f"(//input[@aria-label='Please enter OTP character 1']'])[{c}]").send_keys(f"{otp[ele]}")
        c += 1

# Verify OTP
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Proceed to the next page



# Check if the login was successful
print(driver.title)
if driver.title == "My Benefits":
    print("Login Successful")
else:
    print("Login Failed")
