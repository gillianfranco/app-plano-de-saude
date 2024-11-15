# app-plano-de-saude
**Descrição:** Projeto para praticar lógica de programação em Python, que calcula a mensalidade de um plano de saúde com base em um valor fixo e na idade do cliente.

## Try yourself!
**Proposta:** Imagine que você é um dos programadores responsáveis pela construção de um app para uma empresa X que vende planos de saúde. Uma das estratégias dessa empresa é cobrar um valor diferente com base na idade do cliente, conforme a listagem abaixo:

- Se a idade for maior ou igual a 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100).
- Se a idade for maior ou igual a 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100).
- Se a idade for maior ou igual a 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100).
- Se a idade for maior ou igual a 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100).
- Se a idade for maior ou igual a 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100).
- Se a idade for maior ou igual a 59, o valor será de 600% do valor base do plano (600 / 100).

O valor mensal do plano é calculado da seguinte maneira:

$$valorMensal = valorBase * porcentagem$$

Exemplo: Se o `valorBase` informado for 100,00 e a idade for 45 anos (240% segundo a tabela acima):

$$valorMensal = 100.00 * (240 / 100) = R$ 240,00$$