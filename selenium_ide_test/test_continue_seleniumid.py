# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test_Testcontinue():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcontinue(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'shopping_cart_container\']/a").click()
    self.driver.find_element(By.ID, "checkout").click()
    self.driver.find_element(By.ID, "first-name").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("MEHTAP ")
    self.driver.find_element(By.ID, "last-name").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("TUNÇ")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("34105")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.close()
    currentUrl="https://www.saucedemo.com/checkout-step-two.html"
    assert currentUrl == "https://www.saucedemo.com/checkout-step-two.html"
  
