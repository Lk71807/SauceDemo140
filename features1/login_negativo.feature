Feature: Login Negativo

Scenario Outline: Login Negativo
    Given acesso o site Giuliana Flores
    And clico perfil
    When coloco nos campos de login com E-mail ou CPF <E-mail ou CPF> e senha <senha>
    Then exibe a mensagem de erro no login "<mensagem>"

Examples:
    | id | E-mail ou CPF         | senha       | mensagem                                                                   |
    | 01 | joaomaria@hotmail.com | laranja     | Epic sadface: Username and password do not match any user in this service  |
    | 02 | s278 408 308 24       |             | Epic sadface: Password is required                                         |
    | 03 | saojoao@hotmail.com   | 61093188    | Epic sadface: Username is required                                         |
    | 04 | 306.444.666.25        | amarelo     | Epic sadface: Username and password do not match any user in this service  |
    | 05 | maria@outlook.com     | 61093188    | Epic sadface: Username and password do not match any user in this service  |
    | 06 | fernando@outlook.com  | JM61093188* | Epic sadface: Password is required                                         |
    | 07 |                       |             | Epic sadface: Username is required                                         |
    | 08 | 200 400 500 35        | laranja     | Epic sadface: Username is required                                         |
