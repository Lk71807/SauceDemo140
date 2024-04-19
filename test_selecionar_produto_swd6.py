from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o driver do Selenium
driver = webdriver.Chrome()

# Abre o site
driver.get("https://www.saucedemo.com/")

# Realiza o login
driver.find_element(By.CSS_SELECTOR, ".login_credentials_wrap-inner").click()
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

# Verifica se o login foi bem-sucedido
assert driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

# Adiciona um item ao carrinho
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

# Verifica se o item foi adicionado ao carrinho
assert driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1"

# Abre o carrinho
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()

# Verifica se o carrinho está correto
assert driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
assert driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
assert driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"
assert driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"

# Remove o item do carrinho
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()

# Faz logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)  # Espera 2 segundos para o menu abrir completamente
driver.find_element(By.ID, "logout_sidebar_link").click()

# Fecha o navegador
driver.quit()