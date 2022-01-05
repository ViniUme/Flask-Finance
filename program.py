from flask import Flask, render_template
import requests
import json

from Moedas import Moedas

app = Flask(__name__)

@app.route("/")
@app.route("/moedas")
def home():
    
    names = ["USD", "EUR", "GBP", "ARS", "CAD", "AUD", "JPY", "CNY", "BTC"]
    moedas_url = json.loads(requests.get(f"https://api.hgbrasil.com/finance/quotations?format=debug&key=a99c1c5e").text)
    list_moedas = []
    
    moedas_url = moedas_url["results"]["currencies"]
    
    for itens in names:
        url = moedas_url[itens]
        
        abre = itens
        nome = url["name"]
        preco = round(float(url["buy"]), 2)
        preco = '{0:_}'.format(preco).replace('.',',').replace('_','.')
        variacao = float(url["variation"])
        list_moedas.append(Moedas(abre, nome, preco, variacao))
    
    
    return render_template("home-moedas.html", list_moedas = list_moedas)

if (__name__ == "__main__"):
    app.run(debug=True)