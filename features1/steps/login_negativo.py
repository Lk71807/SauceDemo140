from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'acesso o site Giuliana Flores')
def step_acesso_site(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.giulianaflores.com.br")
    # Aguarde o site carregar
    context.driver.implicitly_wait(10)

@when(u'clico perfil')
def step_clico_perfil(context):
    perfil_button = context.driver.find_element(By.ID, "perfilButton")  # Substitua pelo ID ou outro seletor real do botão de perfil
    perfil_button.click()

@when(u'coloco nos campos de login com E-mail ou CPF {email} e senha {senha}')
def step_coloco_campos_login(context, email, senha):
    email_field = context.driver.find_element(By.ID, "loginEmail")  # Substitua pelo ID ou outro seletor real do campo de email
    password_field = context.driver.find_element(By.ID, "loginPassword")  # Substitua pelo ID ou outro seletor real do campo de senha
    email_field.send_keys(email)
    password_field.send_keys(senha)
    login_button = context.driver.find_element(By.ID, "loginButton")  # Substitua pelo ID ou outro seletor real do botão de login
    login_button.click()

@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)   # preencher o usuario
    # Não preencho a senha
    context.driver.find_element(By.ID, "login-button").click()           # clicar no botão login

@then(u'exibe a mensagem de erro no login "{mensagem}"')
def step_exibe_mensagem_erro(context, mensagem):
    error_message = context.driver.find_element(By.CSS_SELECTOR, ".mensagem-erro")  
    assert mensagem in error_message.text
    context.driver.quit()
