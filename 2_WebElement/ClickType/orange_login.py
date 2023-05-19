from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1 : launch Browser
driver = webdriver.Firefox()

# Step 2 : Open Login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

# Step 3 : Type Username
Username = driver.find_element(By.NAME, "username")
Username.send_keys("Admin")

# Step 4 : Type Password
Password = driver.find_element(By.NAME, "password")
Password.send_keys("admin123")

# Step 5 : Click Login button
login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")
login_button.click()
time.sleep(5)

# Step 6 : Logout
profile = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
profile.click()

logout = driver.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(4) > a:nth-child(1)")
logout.click()

driver.close()

