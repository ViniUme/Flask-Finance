from flask import Flask, render_template
import requests
import json

class Moedas():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

app = Flask(__name__)

@app.route("/")
@app.route("/moedas")
def home():
    
    names = ["USD", "EUR", "GBP", "ARS", "CAD", "AUD", "JPY", "CNY", "BTC"]
    const_url = json.loads(requests.get(f"https://api.hgbrasil.com/finance").text)
    list_moedas = []
    
    const_url = const_url["results"]["currencies"]
    
    for itens in names:
        url = const_url[itens]
        
        nome = url["name"]
        preco = url["buy"]
        list_moedas.append(Moedas(nome, preco))
    
    
    return render_template("home-moedas.html", list_moedas = list_moedas)

if (__name__ == "__main__"):
    app.run(debug=True)