from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://pypi.python.org/pypi")
driver.find_element(By.ID, "term").send_keys("Selenium")
driver.find_element(By.ID, "submit").click()
driver.quit()
