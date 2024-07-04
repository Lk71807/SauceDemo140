Feature: Criando usuário

      Scenario: Criação de usuário "login/cadastrar"
          Given que acesso o site Giuliana Flores
          When preencho os campos de login/cadastrar com Nome Completo "João Maria", CPF "123.456.789-00", E-mail "joaomaria@hotmail.com", senha "JM61093188*", endereço "Rua das Flores, 123" e telefone "11987654321"
          Then sou direcionado a página Home


