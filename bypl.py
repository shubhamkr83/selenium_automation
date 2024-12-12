import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Open the initial URL
BYPL = ("https://byplrewards.thriwe.com/rewards?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJjYU51bWJlciI6IjE1MzY5NjY0MiIsImN1c3RvbWVyTmFtZSI6Ik1yLiBHT1BBTCAgQkhBUkRXQUoifQ.jpFSbO6TNLyP5WzdpiiK"
        "-5xsk3y8tZswdcanO_nvA-I")
driver.get(BYPL)

# ------------------Web Url-------------------------
Home_url = "https://byplrewards.thriwe.com/home"
History_url = "https://byplrewards.thriwe.com/history"
Terms_url = "https://byplrewards.thriwe.com/term-and-condition"
Faq_url = "https://byplrewards.thriwe.com/faq"
Privacy_url = "https://byplrewards.thriwe.com/privacypolicy"
Earnpoint_url = "https://byplrewards.thriwe.com/earnpoints"
Contact_url = "https://byplrewards.thriwe.com/contactus"

# ------------------Header Locators----------------
Home_btn = driver.find_element(By.CSS_SELECTOR,
                               "body > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                               "div:nth-child(3)")
History_btn = driver.find_element(By.XPATH,
                                  "//div[@class='d-none d-lg-block'][normalize-space()='My Redemption History']")
Terms_btn = driver.find_element(By.XPATH, "//div[@class='d-none d-lg-block'][normalize-space()='T&C']")
Faq_btn = driver.find_element(By.XPATH, "//div[@class='d-none d-lg-block'][normalize-space()='FAQS']")
Privacy_btn = driver.find_element(By.XPATH, "//div[@class='d-none d-lg-block'][normalize-space()='Privacy Policy']")
Earnpoint_btn = driver.find_element(By.XPATH, "//div[@class='d-none d-lg-block'][normalize-space()='Earn points']")
Contact_btn = driver.find_element(By.XPATH, "//div[@class='d-none d-lg-block'][normalize-space()='Contact Us']")

# -----------------Url Check-------------------
print("BYPL Website Checking...")


def check_url(name, expected_url):
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url))
    current_url = driver.current_url
    if current_url == expected_url:
        print(f"{name} URL matched")
    else:
        print(f"{name} URL did not match")
        print(f"Expected URL: {expected_url}, but got: {current_url}")


# ----------------Homepage url check--------------
Home_btn.click()
check_url("Home", Home_url)

# ----------------History url check--------------
History_btn.click()
check_url("History", History_url)

# ----------------Term url check--------------
Terms_btn.click()
check_url("Term", Terms_url)

# ----------------FAQ url check--------------
Faq_btn.click()
check_url("FAQ", Faq_url)

# ----------------Privacy url check--------------
Privacy_btn.click()
check_url("Privacy", Privacy_url)

# ----------------Earnpoint url check--------------
Earnpoint_btn.click()
check_url("Earnpoint", Earnpoint_url)

# ----------------Contact url check--------------
Contact_btn.click()
check_url("Contact", Contact_url)

# Close the driver
driver.quit()
