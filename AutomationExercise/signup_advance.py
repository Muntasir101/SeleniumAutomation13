from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random


def random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(5))
    domain_name = random.choice(domain)
    email = f"{username}@{domain_name}"
    return email


def random_string():
    letters = string.ascii_lowercase + string.digits
    random_name = ''.join(random.choice(letters) for _ in range(8))
    string_random = f"{random_name}"
    return random_name


def random_number():
    numbers = string.digits
    random_numbers = ''.join(random.choice(numbers) for _ in range(8))
    string_random = f"{random_numbers}"
    return numbers


user_credentials = [random_email(), random_number()]

# Step 1 : Launch Browser
driver = webdriver.Firefox()

# Step 2 : Open Home page
driver.get("https://automationexercise.com/")
time.sleep(5)

# Verify that home page is visible successfully
expected_home_page_url = "https://automationexercise.com/"
actual_home_page_url = driver.current_url

try:
    assert expected_home_page_url == actual_home_page_url
    print("Home page is visible successfully.")
except AssertionError:
    print("home page is not visible successfully")

driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a").click()

#  Verify 'New User Signup!' is visible
expected_signup_page_text = "New User Signup!"
actual_signup_page_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form h2")))
actual_signup_page_text = actual_signup_page_element.text

try:
    assert expected_signup_page_text == actual_signup_page_text
    print("'New User Signup!' is visible")

except:
    print("'New User Signup!' is not visible")

try:
    # Step 3 : Type Username
    Username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    Username.send_keys(random_string())
except :
    print("Username Locator Changed.")

# Step 4 : Type Email
try:
    Email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form > form:nth-child(2) > input:nth-child(3)")))
    Email.send_keys(user_credentials[0])
except :
    print("Email Locator Changed.")

# Step 5 : Click Signup button
signup_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(5)")))
signup_button.click()



# Step 6 : Click Title button
title_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.radio-inline:nth-child(3) > label:nth-child(1)")))
title_button.click()

# Step 7 : Type Password
Password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
Password.send_keys(user_credentials[1])

# Step 8 : Click Date of birth
date = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#days"))))
date.select_by_visible_text("10")

month = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#months"))))
month.select_by_visible_text("May")

year = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#years"))))
year.select_by_visible_text("2010")

# Step 9 : Address info
try:
    Firstname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first_name")))
    Firstname.send_keys(random_string())
except:
    print("Firstname not found.")

Lastname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "last_name")))
Lastname.send_keys(random_string())

Address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "address1")))
Address.send_keys(random_string())

# Country
Country = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='country']"))))
Country.select_by_visible_text("Canada")

State = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "state")))
State.send_keys(random_string())

City = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "city")))
City.send_keys(random_string())

Zipcode = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "zipcode")))
Zipcode.send_keys("700001")

Mobile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mobile_number")))
Mobile.send_keys("123456789")

Create = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[action] .btn-default")))
Create.click()

print(user_credentials)
