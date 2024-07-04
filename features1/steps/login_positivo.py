from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que entro no site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.giulianaflores.com.br")
    context.driver.maximize_window()

@when(u'preencho os campos de login com E-mail ou CPF "{email}" e senha "{senha}"')
def step_impl(context, email, senha):
    wait = WebDriverWait(context.driver, 10)
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login")))  # Verifique o ID do botão de login
    login_button.click()
    context.driver.find_element(By.ID, "email_or_cpf").send_keys(email)  # Verifique o ID do campo de email ou CPF
    context.driver.find_element(By.ID, "password").send_keys(senha)  # Verifique o ID do campo de senha
    context.driver.find_element(By.ID, "login_submit").click()  # Verifique o ID do botão de submissão do login

@then(u'exibe a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    wait = WebDriverWait(context.driver, 10)
    mensagem_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "elemento-que-contem-a-mensagem")))  # Verifique o seletor do elemento que contém a mensagem
    assert mensagem in mensagem_element.text
    context.driver.quit()
