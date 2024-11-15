# Valida se o valor informado pelo usuário é maior que zero
def valida_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            while valor < 0:
                valor = float(input('\nValor inválido! Digite um valor maior que zero: '))
            print()
            break
        except ValueError:
            print('\nValor inválido! Tente novamente.')

    return valor

# Calcula qual a mensalidade que deve ser paga de acordo com o valor base do plano e a idade informada
def calcula_mensalidade(base, idade):
    if (idade >= 0) and (idade < 19):
        mensalidade = base * (100 / 100)
    elif (idade >= 19) and (idade < 29):
        mensalidade = base * (150 / 100)
    elif (idade >= 29) and (idade < 39):
        mensalidade = base * (225 / 100)
    elif (idade >= 39) and (idade < 49):
        mensalidade = base * (240 / 100)
    elif (idade >= 49) and (idade < 59):
        mensalidade = base * (350 / 100)
    else:
        mensalidade = base * (600 / 100)

    return mensalidade

# Solicita que o usuário informe o valor base do plano
valor_base = valida_valor('Digite o VALOR BASE do plano: ')

# Solicita que o usuário informe a idade do cliente
idade_cliente = int(valida_valor('Digite a IDADE do cliente: '))

# Recebe o valor da mensalidade que o cliente deve pagar
valor_mensal = calcula_mensalidade(valor_base, idade_cliente)

print(f'Valor mensal do plano: R${valor_mensal:.2f}')
