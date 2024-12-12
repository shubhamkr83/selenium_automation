from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from email_otp import Otp

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
URL = "https://stag-dib.thriwe.com/login"
driver.get(URL)
driver.maximize_window()

# Select the dropdown option
dd_obj1 = driver.find_element("xpath", "//select[@id='select']")
dd1 = Select(dd_obj1)
dd1.select_by_value('8')

# Enter mobile number and login
driver.find_element("xpath", "//input[@placeholder='Enter Mobile Number']").send_keys("8888889")
driver.find_element("xpath", "//div[text()='Login']").click()

# Wait for the OTP to arrive and be extracted
sleep(5)
username = "automationdib@gmail.com"
password = "ozwg ptkc xcnq koqk"
imap_server = "imap.gmail.com"
otp = Otp(username, password, imap_server).extract_otp_from_email()

# Input the OTP
c = 1
for ele in range(0, len(otp)):
    if c != 7:
        driver.find_element("xpath", f'(//input)[{c}]').click()
        driver.find_element("xpath", f'(//input)[{c}]').send_keys(f'{otp[ele]}')
        c += 1

# Verify OTP
driver.find_element("xpath", "//div[text()='Verify']").click()

# Proceed to the next page
sleep(2)
driver.find_element("xpath", "//button[text()='Click to Proceed']").click()
sleep(5)

# Check if the login was successful
print(driver.title)
if driver.title == "My Benefits":
    print("Login Successful")
else:
    print("Login Failed")

# Commented out code for future actions
# action_chain = ActionChains(driver)
# sleep(1)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sleep(2)
# driver.find_element("xpath", "(//button[text()='Book Now'])[1]").click()
# sleep(2)
# driver.execute_script("window.scrollTo(0, 350);")
# sleep(1)
# driver.find_element("xpath", "(//button[text()='Book Now'])[1]").click()
# sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
