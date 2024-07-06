Feature: compra banner

  Scenario: compra banner "Cacau Show"
    Given acesso no site Cacau Show
    When clico em chocolate e Trufas lacreme 160g adicionar ao carrinho uma vez
    And clico no carrinho para conferir a compra
    Then clico em remover compra e o site pergunta se deseja remover o produto do carrinho clico sim
