# Generated by Selenium IDE
import pytest                # framework de teste de unidade
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSelecionarProduto():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {} 
    self.driver.implicitly_wait(5) # irá esoerar qualquer elemento por até 5 segundos <-- Melhor

  def teardown_method(self, method):
    self.driver.quit()
  
  def test_selecionarProduto(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".login_credentials_wrap-inner").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, ".login_password").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    assert self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1"
    self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
    assert self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2) # parando o processamento / thread por 2 segundos <-- Pior - uso apenas temporário
    self.driver.find_element(By.ID, "logout_sidebar_link").click()
  
