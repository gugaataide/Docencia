from flask import Flask, render_template, request, flash, redirect,url_for
from datetime import datetime

app = Flask(__name__)


def validar_cvv(cvv):
    # Verificar se o CVV contém apenas dígitos e tem 3 ou 4 dígitos (dependendo da rede)
    if not cvv.isdigit() or not (len(cvv) == 3 or len(cvv) == 4):
        return False
    return True


def validar_data_vencimento(data_vencimento):
    try:
        
        # Verificar se a data está no formato MM/AA
        data_formatada = datetime.strptime(data_vencimento, '%m/%y')

        # Verificar se a data não está no passado (ou seja, maior ou igual à data atual)
        data_atual = datetime.now()
        
        if data_formatada < data_atual:
            return False

        return True
    except ValueError:
        return False
    

def validar_cartao(numero_cartao):
    # Remover espaços em branco e hífens
    numero_cartao = numero_cartao.replace(" ", "").replace("-", "")

    # Verificar se o número do cartão é composto apenas por dígitos
    if not numero_cartao.isdigit():
        return False

    # Verificar a quantidade de dígitos (geralmente 13 a 19 dígitos para números de cartão de crédito)
    if not (13 <= len(numero_cartao) <= 19):
        return False

    # Aplicar o Algoritmo de Luhn (Algoritmo de Modulus 10)
    reversed_digits = numero_cartao[::-1]
    soma = 0
    for i, d in enumerate(reversed_digits):
        digito = int(d)
        if i % 2 == 1:
            digito = digito * 2
            if digito > 9:
                digito -= 9
        soma += digito

    if soma % 10 != 0:
        return False

    # Verificar a rede do cartão (exemplo: Visa começa com 4, MasterCard com 5)
    if numero_cartao[0] == '4':
        rede = 'Visa'
    elif numero_cartao[0] == '5':
        rede = 'MasterCard'
    elif numero_cartao[0] == '6':
        rede = 'Elo'
    else:
        rede = 'Desconhecida'

    return rede




@app.route('/', methods=['GET', 'POST'])
def formulario_pagamento():
    mensagem = None

    if request.method == 'POST':
        
        nome = request.form.get('nome')
        numero_cartao = request.form.get('numero-cartao')
        vencimento = request.form.get('vencimento')
        cvv = request.form.get('cvv')

        rede = validar_cartao(numero_cartao)
        if not nome or not numero_cartao or not vencimento or not cvv:
            mensagem = "Todos os campos são obrigatórios."
        elif not rede:
            mensagem = "Número de cartão inválido."
        elif not validar_cvv(cvv):
            mensagem = "CVV inválido."
        elif not validar_data_vencimento(vencimento):
            mensagem = "Data inválida"
        else:
            mensagem = f"Pagamento aceito para {nome}. O número do cartão é válido ({rede})."
            ACEITO_SIM_NAO = True
        if ACEITO_SIM_NAO == True:
            redirect(url_for, )

    return render_template('cartao.html', mensagem=mensagem)



if __name__ == '__main__':
    app.run(debug=True)