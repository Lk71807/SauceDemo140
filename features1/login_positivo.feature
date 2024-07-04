Feature: Login positivo
Scenario Outline: Login positivo
        Given que entro no site Giuliana Flores
        When preencho os campos de login com E-mail ou CPF <joaomaria@hotmail.com> e senha <JM61093188*>
        Then exibe a <mensagem> Boa Tarde, Joao!
