from flask import Flask, render_template, request, redirect
from estrutura.tabela_hash import TabelaHash
from persistencia import carregar_dados, salvar_dados

app = Flask(__name__)
tamanho = 53
tabela_paises = TabelaHash(tamanho)

dados_iniciais = carregar_dados()
for pais in dados_iniciais:
    conseguiu = tabela_paises.inserir(pais)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/inserir")
def inserir():

    novo_pais = {
        "codigo": request.form["codigo"],
        "pais": request.form["pais"],
        "regiao": request.form["regiao"],
        "operadora": request.form["operadora"],
        "tecnologia": request.form["tecnologia"]
    }

    inserido = tabela_paises.inserir(novo_pais)
    

