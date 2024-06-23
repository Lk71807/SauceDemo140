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

class TestCriaodeusurio():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_criaodeusurio(self):
    self.driver.get("https://www.giulianaflores.com.br/")
    self.driver.set_window_size(1296, 688)
    self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    self.driver.find_element(By.ID, "ContentSite_txtName").click()
    self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Joao Maria")
    self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
    self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("309.267.470-70")
    self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("joaomaria@hotmail.com")
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("JM61093188*")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("03982-190")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("03982150")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("590")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
    element = self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11980405060")
    self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
    self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("427")
    self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
    self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
    element = self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
    self.driver.execute_script("window.scrollTo(0,228)")
    self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "perfil-hidden").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()