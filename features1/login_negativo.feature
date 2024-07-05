feature: login Negativo

        Scenario Outline: Login Negativo
        Given que entro no site Giuliana Flores
        End clico em perfil
        When preencho os campos de login com E-mail ou CPF <joaomaria@hotmail.com> e senha <JM61093188*>
        Then exibe a <mensagem> de erro no login


        Examples:
        | id | E-mail ou CPF                         | senha        | mensagem                                                                   |
        | 01 | joaomaria@hotmail.com                 | laranja      | Epic sadface: Username and password do not match any user in this service  |
        | 02 | s278 408 308 24                       |              | Epic sadface: Password is required                                         |
        | 03 | saojoao@hotmail.com                   | 61093188     | Epic sadface: Username is required                                         |
        | 04 | 306.444.666.25                        | amarelo      | Epic sadface: Username and password do not match any user in this service  |
        | 05 | maria@outlook.com                     | 61093188     | Epic sadface: Username and password do not match any user in this service  |
        | 06 | fernando@outlook.com                  | JM61093188*  | Epic sadface: Password is required                                         |
        | 07 |                                       |              | Epic sadface: Username is required                                         |
        | 08 | 200 400 500 35                        | laranja      | Epic sadface: Username is required                                         |
