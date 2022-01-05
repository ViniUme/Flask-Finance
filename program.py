from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
@app.route("/moedas")
def Home():

    from Moedas import Moedas

    names = ["USD", "EUR", "GBP", "ARS", "CAD", "AUD", "JPY", "CNY", "BTC"]
    api_url = json.loads(requests.get(f"https://api.hgbrasil.com/finance/quotations?format=debug&key=a99c1c5e").text)
    list_moedas = []
    
    api_url = api_url["results"]["currencies"]
    
    for itens in names:
        url = api_url[itens]
        
        abre = itens
        nome = url["name"]
        preco = round(float(url["buy"]), 2)
        preco = '{0:_}'.format(preco).replace('.',',').replace('_','.')
        variacao = url["variation"]
        list_moedas.append(Moedas(abre, nome, preco, variacao))
    
    
    return render_template("home-moedas.html", list_moedas = list_moedas)

@app.route("/bitcoin")
def Bitcoin():

    from Bitcoin import Bitcoin

    names = ["blockchain_info" , "coinbase" , "bitstamp" , "foxbit" , "mercadobitcoin"]
    api_url = json.loads(requests.get(f"https://api.hgbrasil.com/finance/quotations?key=a99c1c5e").text)

    list_bitcoin = []

    api_url = api_url["results"]["bitcoin"]

    for itens in names:

        url = api_url[itens]

        nome = url["name"]
        preco = round(float(url["last"]), 2)
        preco = '{0:_}'.format(preco).replace('.',',').replace('_','.')
        variacao = url["variation"]

        list_bitcoin.append(Bitcoin(nome, preco, variacao))

    return render_template("bitcoin-page.html", list_bitcoin = list_bitcoin)

if (__name__ == "__main__"):
    app.run(debug=True)