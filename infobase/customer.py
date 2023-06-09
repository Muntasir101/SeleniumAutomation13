import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Step 1 : Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2 : Open Login page
driver.get("https://infobase.ispms.net/")
time.sleep(5)

# Step 3 : Type Username
Username = driver.find_element(By.NAME, "user_name")
Username.send_keys("test")

# Step 4 : Type Email
password = driver.find_element(By.NAME, "password")
password.send_keys("1234@")

# Step 5 : Click Signup button
signup_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
signup_button.click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(4) > a > span").click()

driver.find_element(By.CSS_SELECTOR, "[href='create_home_user\.php']").click()

driver.find_element(By.CSS_SELECTOR, "span#select2-dist_id-container").click()
time.sleep(3)

action = ActionChains(driver)
action.key_down(Keys.DOWN).key_up(Keys.DOWN).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

time.sleep(10)