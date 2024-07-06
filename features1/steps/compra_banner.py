from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup do webdriver
driver = None

@given(u'acesso no site Cacau Show')
def step_impl(context):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.cacaushow.com.br")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Chocolate"))
    )

@when(u'clico em chocolate e Trufas lacreme 160g adicionar ao carrinho uma vez')
def step_impl(context):
    chocolate_menu = driver.find_element(By.LINK_TEXT, "Chocolate")
    chocolate_menu.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Trufas LaCreme 160g"))
    )

    trufas_produto = driver.find_element(By.LINK_TEXT, "Trufas LaCreme 160g")
    trufas_produto.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Adicionar ao carrinho']"))
    )

    adicionar_ao_carrinho = driver.find_element(By.XPATH, "//button[text()='Adicionar ao carrinho']")
    adicionar_ao_carrinho.click()

@when(u'clico no carrinho para conferir a compra')
def step_impl(context):
    carrinho = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "carrinho"))
    )
    carrinho.click()

@then(u'clico em remover compra e o site pergunta se deseja remover o produto do carrinho clico sim')
def step_impl(context):
    remover_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Remover']"))
    )
    remover_button.click()

    confirmar_remocao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Sim']"))
    )
    confirmar_remocao.click()

    driver.quit()
