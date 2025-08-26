import requests
from datetime import datetime, timedelta

#definindo função de câmbio
def buscar_cotacao():
    dias = 0
    while dias < 7:
        data = (datetime.now() - timedelta(days=dias)).strftime("%m-%d-%Y")
        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao='{data}')?$top=1&$format=json"
        response = requests.get(url)
        dados = response.json()
        if dados["value"]:
            return dados["value"][0]["cotacaoCompra"]
        dias += 1
    return None

def converter_moeda(valor):
    cotacao = buscar_cotacao()
    if cotacao:
        return valor * cotacao
    else:
        return None
    
valor_dolar = float(int(input("Digite o valor em dólar: ")))
conversao = converter_moeda(valor_dolar)
if conversao:
    print(f"O valor de US$ {valor_dolar} em reais é: R$ {conversao}.")
else:
    print("Não foi possível realizar a conversão.")
