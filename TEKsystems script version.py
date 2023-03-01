# TEKsystems/Werner tech challenge. Script version: Buy socks on Amazon

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://amazon.com/")

# Search for socks
try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search.click()
    search.clear()
    search.send_keys("socks")
    search.submit()
except:
    driver.quit()

# Click on the first search result
try:
    socks = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "s-image"))
    )
    socks.click()
except:
    driver.quit()

# Add the item to the cart
try:
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-button"))
    )
    add_to_cart.click()
except:
    driver.quit()

# Proceed to checkout
try:
    checkout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "desktop-ptc-button-celWidget"))
    )
    checkout.click()
except:
    driver.quit()
