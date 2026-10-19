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

@app.route("/inserir_pais", methods=["POST"])
def inserir():
    codigo_limpo = request.form.get("codigo", "").strip().upper()
    
    novo_pais = {
        "codigo": codigo_limpo,
        "ddi": request.form.get("ddi"),
        "pais": request.form.get("pais"),
        "regiao": request.form.get("regiao"),
        "operadora": request.form.get("operadora"),
        "tecnologia": request.form.get("tecnologia")
    }

    inserido = tabela_paises.inserir(novo_pais)

    if inserido:
        salvar_dados(tabela_paises.listar_paises())
    
    return redirect("/listagem_paises")

@app.route("/buscar_pais", methods=["GET"])
def buscar_pais():
    codigo_limpo = request.args.get("codigo", "").strip().upper()
    pais = tabela_paises.buscar(codigo_limpo)
    return render_template("paises.html", pais=pais)

@app.route("/listagem_paises")
def listar_paises():
    lista_paises = tabela_paises.listar_paises()
    return render_template("paises.html", paises=lista_paises)

@app.route("/alterar_pais", methods=["POST"])
def alterar_pais():
    codigo_limpo = request.form.get("codigo", "").strip().upper()
    ddi = request.form.get("ddi")
    pais = request.form.get("pais")
    regiao = request.form.get("regiao")
    operadora = request.form.get("operadora")
    tecnologia = request.form.get("tecnologia")

    alterado = tabela_paises.alterar(codigo_limpo, ddi, pais, regiao, operadora, tecnologia)
    
    if alterado:
        salvar_dados(tabela_paises.listar_paises())
        
    return redirect("/listagem_paises")

@app.route("/remover_pais", methods=["POST"])
def remover_pais():
    codigo_limpo = request.form.get("codigo", "").strip().upper()
    removido = tabela_paises.remover(codigo_limpo)

    if removido:
        salvar_dados(tabela_paises.listar_paises())
        
    return redirect("/listagem_paises")

if __name__ == "__main__":
    app.run(debug=True)