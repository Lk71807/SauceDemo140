from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que acesso o site Giuliana Flores')
def step_given_acesso_site(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.giulianaflores.com.br")
    context.driver.maximize_window()

@when('preencho os campos de login/cadastrar com Nome Completo "{nome}", CPF "{cpf}", E-mail "{email}", senha "{senha}", endereço "{endereco}" e telefone "{telefone}"')
def step_when_preencho_campos(context, nome, cpf, email, senha, endereco, telefone):
    wait = WebDriverWait(context.driver, 20)  # Aumente o tempo de espera para 20 segundos
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login")))
    login_button.click()
    register_button = wait.until(EC.presence_of_element_located((By.ID, "register")))
    register_button.click()
    context.driver.find_element(By.ID, "nome_completo").send_keys(nome)
    context.driver.find_element(By.ID, "cpf").send_keys(cpf)
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "senha").send_keys(senha)
    context.driver.find_element(By.ID, "endereco").send_keys(endereco)
    context.driver.find_element(By.ID, "telefone").send_keys(telefone)
    context.driver.find_element(By.ID, "cadastrar").click()

@then('sou direcionado a página Home')
def step_then_sou_direcionado_pagina_home(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.title_contains("Home"))
    assert "Home" in context.driver.title
    context.driver.quit()
