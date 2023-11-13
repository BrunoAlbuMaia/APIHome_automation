import json


class GestorHidroJSON:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
       
        
    def ler_dados_json(self):
        try:
            with open(self.nome_arquivo, "r") as arquivo_json:
                self.dados = json.load(arquivo_json)
                return self.dados
        except FileNotFoundError:
            return None

    def atualizar_dados(self, id_equipamento, valorcm):
        try:
            for equipamento in self.dados:
                if equipamento["IdEquipamento"] == id_equipamento:
                    
                   equipamento.update({'valorOcupadoAgua': valorcm})
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
        
# dadosJson = GestorHidroJSON("src/data/dadoHidro.json")
# dadosJson.ler_dados_json()
# dadosJson.atualizar_dados(1,15)