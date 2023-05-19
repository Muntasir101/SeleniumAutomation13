from selenium import webdriver

# Launch Browser
driver = webdriver.Firefox()

# Open Website
driver.get("https://google.com/")

# Close Current Tab
#driver.close()
driver.quit()
