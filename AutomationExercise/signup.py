from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


# Step 1 : Launch Browser
driver = webdriver.Firefox()

# Step 2 : Open Login page
driver.get("https://automationexercise.com/login")
time.sleep(5)

# Step 3 : Type Username
Username = driver.find_element(By.NAME, "name")
Username.send_keys("Pnt")

# Step 4 : Type Email
Email = driver.find_element(By.CSS_SELECTOR, ".signup-form > form:nth-child(2) > input:nth-child(3)")
Email.send_keys("pnt12@pnt2.com")

# Step 5 : Click Signup button
signup_button = driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(5)")
signup_button.click()
time.sleep(5)

# Step 6 : Click Title button
title_button = driver.find_element(By.CSS_SELECTOR, "div.radio-inline:nth-child(3) > label:nth-child(1)")
title_button.click()

# Step 7 : Type Password
Password = driver.find_element(By.NAME, "password")
Password.send_keys("123456")

# Step 8 : Click Date of birth
date = Select(driver.find_element(By.CSS_SELECTOR, "#days"))
date.select_by_visible_text("10")
time.sleep(2)

month = Select(driver.find_element(By.CSS_SELECTOR, "#months"))
month.select_by_visible_text("May")
time.sleep(2)

year = Select(driver.find_element(By.CSS_SELECTOR, "#years"))
year.select_by_visible_text("2010")
time.sleep(2)


# Step 9 : Address info
Firstname = driver.find_element(By.NAME, "first_name")
Firstname.send_keys("Nazmus")

Lastname = driver.find_element(By.NAME, "last_name")
Lastname.send_keys("Sakib")

Address = driver.find_element(By.NAME, "address1")
Address.send_keys("Road 17 house 18")

# Country
Country = Select(driver.find_element(By.CSS_SELECTOR, "[name='country']"))
Country.select_by_visible_text("Canada")

State = driver.find_element(By.NAME, "state")
State.send_keys("Kolkata")

City = driver.find_element(By.NAME, "city")
City.send_keys("Kolkata")

Zipcode = driver.find_element(By.NAME, "zipcode")
Zipcode.send_keys("700001")

Mobile = driver.find_element(By.ID, "mobile_number")
Mobile.send_keys("123456789")

Create = driver.find_element(By.CSS_SELECTOR, "[action] .btn-default")
Create.click()


