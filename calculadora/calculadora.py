def calculadora():
    operacao = input('''
Escolha a operação desejada:
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão
''')

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if operacao == '+':
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))

    elif operacao == '-':
        sub = n1 - n2
        print('{} - {} = {}'.format(n1, n2, sub))

    elif operacao == '*':
        mult = n1 * n2
        print('{} * {} = {}'.format(n1, n2, mult))

    elif operacao == '/':
        div = n1 / n2
        print('{} / {} = {}'.format(n1, n2, div))

    else:
        print('Operação inválida')

    repetir()

def repetir():
    repetir_calc = input('''
Deseja usar a calculadora novamente? (Sim/Não)
''')

    if repetir_calc.upper() == 'SIM':
        calculadora()
    elif repetir_calc.upper() == 'NÃO':
        print('Até logo.')
    else:
        repetir()

calculadora()
