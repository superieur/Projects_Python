Gasto = []
Total = []
Lucro = []

def calculo():
    global Gasto
    global Total
    global Lucro
    while True:
        try:
            peso = float(input('Peso:'))
        except ValueError:
            print('Inválido')
            continue
        else:
            break
    while True:
        try:
            compra = float(input('Valor de compra:'))
        except ValueError:
            print('Inválido')
            continue
        else:
            break
    while True:
        try:
            venda = float(input('Valor de venda:'))
        except ValueError:
            print('Inválido')
            continue
        else:
            break
    print(f'O peso é {peso}, o valor da compra é {compra} e o valor da venda é {venda}.')
    d = input('CORRETO? ')
    if d == 'n' or d == 'nao':
        calculo()
    else:
        Total_produto = peso * venda
        Gasto_produto = peso * compra
        Lucro_produto = Total_produto - Gasto_produto
        Gasto += [Gasto_produto]
        Total += [Total_produto]
        Lucro += [Lucro_produto]
        print('Total recebido:', Total_produto)
        print('Valor gasto :', Gasto_produto)
        print('Lucro:', Lucro_produto)
        d = input('CONTINUAR? ')
        if d == 'nao' or d == 'n':
            return
        else:
            calculo()

def apresentar_valores(gasto,total,lucro):
    int_gasto = map(int, gasto)
    list_gasto = list(int_gasto)
    gasto_total = sum(list_gasto)

    int_total = map(int, total)
    list_total = list(int_total)
    total_total = sum(list_total)

    int_lucro = map(int, lucro)
    list_lucro = list(int_lucro)
    lucro_total = sum(list_lucro)

    print(f'O valor recebido ao vender: {total_total} ')
    print(f'O valor gasto para comprar: {gasto_total}')
    print(f'O seu lucro foi: {lucro_total}')

calculo()
apresentar_valores(Gasto,Total,Lucro)