import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
EPIFI_URL = ("https://epifi.thriwe.com/rewards?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
             ".eyJmaVVzZXJJZCI6ImUxNGU4MDVlLTgyZWUtNDc2MS1iM2I5LWQ0MzY3OWMzMTNhNCJ9"
             ".zqVTcXjhPG70mRJfI1Ud4wa5RJxPue7_Hvpry9SN9Lg")
HOME_URL = "https://epifi.thriwe.com/dashboard"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Open the EPIFI URL
driver.get(EPIFI_URL)

# -----------------Url Check-------------------
print("EPIFI Website Checking...")

time.sleep(2)


# Function to check URL
def check_url(name, expected_url):
    current_url = driver.current_url
    if current_url == expected_url:
        print(f"{name} URL matched")
    else:
        print(f"{name} URL did not match")
        print(f"Expected URL: {expected_url}, got: {current_url}")


# Wait for the homepage URL to load and check it
print("EPIFI Website Checking...")
try:
    WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))
    check_url("Home", HOME_URL)
except Exception as e:
    print(f"Error: {e}")

# Close the driver
driver.quit()
