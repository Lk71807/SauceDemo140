# Biblioteca
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produtos():

     url = "https://www.saucedemo.com"        



     def setup_method(self, method):                # método de inicialização dos testes
        self.driver = webdriver.Chrome()           # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)            # define o tempo de espera padrão por elementos em 10 segundos

     def teardown_method(self, method):             # método de finalização dos testes
        self.driver.quit() 

     def test_selecionar_produto(self):             # método de teste
        self.driver.get(self.url)                  # abre o navegador
        self.driver.find_element(By.ID , "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()

        #transição de pagina

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99" 
        assert self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click      # add no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"      # entra no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, "item-quantity").text == "1"          # validar carrinho de compra

        # validar produto no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory-item-name").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"

        # Remover o produto
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()   # remove mochila

        # Realiza Lougout

        self.driver.find_element(By.ID, "logout_sidebar_link").click()            # faz logout no site