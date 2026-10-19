class TabelaHash:
    def __init__(self, tamanho:int):
        self.tamanho = tamanho
        self.tabela = {}
    
    def calcula_posicao(self, chave:str) -> int:
        soma_ascii = sum(ord(caractere) for caractere in chave)
        posicao = soma_ascii % self.tamanho
        return posicao
    
    def inserir(self, pais:dict) -> bool:
        codigo = pais["codigo"]
        posicao = self.calcula_posicao(codigo)
        if posicao not in self.tabela:
            self.tabela[posicao] = []

        for item in self.tabela[posicao]:
            if item["codigo"] == codigo:
                return False
            
        self.tabela[posicao].append(pais)
        return True
    
    # Atualizado para receber o DDI
    def alterar(self, codigo:str, ddi:str, pais:str, regiao:str, operadora:str, tecnologia: str) -> bool:
        posicao = self.calcula_posicao(codigo)

        if posicao not in self.tabela:
            return False
        
        for item in self.tabela[posicao]:
            if item["codigo"] == codigo:
                item["ddi"] = ddi
                item["pais"] = pais
                item["regiao"] = regiao
                item["operadora"] = operadora
                item["tecnologia"] = tecnologia
                return True
        return False

    def remover(self, codigo:str) -> bool:
        posicao = self.calcula_posicao(codigo)

        if posicao not in self.tabela:
            return False
        
        for pais in self.tabela[posicao]:
            if pais["codigo"] == codigo:
                self.tabela[posicao].remove(pais)
                return True
        return False

    def listar_paises(self):
        lista_geral = []
        for posicao in self.tabela:
            for pais in self.tabela[posicao]:
                lista_geral.append(pais)
        return lista_geral
    
    def buscar(self, codigo:str):
        posicao = self.calcula_posicao(codigo)

        if posicao not in self.tabela:
            return None
        
        for item in self.tabela[posicao]:
            if item["codigo"] == codigo:
                return item
            
        return None