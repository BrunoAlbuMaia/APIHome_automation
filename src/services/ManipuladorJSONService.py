import json


class GestorDeDadosJSON:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
       
        
    def ler_dados_json(self):
        try:
            with open(self.nome_arquivo, "r") as arquivo_json:
                self.dados = json.load(arquivo_json)
                return self.dados
        except FileNotFoundError:
            return None
    
    def obter_dados_por_id(self, id_equipamento):
        for equipamento in self.dados:
            if equipamento["IdEquipamento"] == id_equipamento:
                return equipamento
        return None  # Retorna None se o ID não for encontrado
      
    def adicionar_dados(self, novo_dado):
        self.dados.append(novo_dado)
        self.salvar_dados_json()

    async def atualizar_dados(self, id_equipamento, novos_dados):
        try:
            for equipamento in self.dados:
                if equipamento["IdEquipamento"] == id_equipamento:
                    equipamento.update(novos_dados)
            self.salvar_dados_json()
        except Exception as ex:
            print(ex)
        
        
    def salvar_dados_json(self):
        try:
            with open(self.nome_arquivo, "w") as arquivo_json:
                print(self.nome_arquivo)
                json.dump(self.dados, arquivo_json, indent=4)
        except Exception as ex:
            print(ex)
        
