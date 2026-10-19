import json
import os

CAMINHO_JSON = os.path.join("arquivos", "paises.json")

def carregar_dados():
    """Lê o arquivo paises.json e retorna a lista de dicionários."""
    if not os.path.exists(CAMINHO_JSON):
        return []
    
    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def salvar_dados(lista_paises):
    """Recebe a lista de países (obtida da Tabela Hash) e grava no JSON."""
    os.makedirs(os.path.dirname(CAMINHO_JSON), exist_ok=True)
    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_paises, f, ensure_ascii=False, indent=4)