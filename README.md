
# API 

A API é um componente fundamental do projeto de automação residencial baseado em ESP32. Sua principal função é armazenar e fornecer dados sobre os equipamentos presentes no ambiente residencial, como lâmpadas e sensores de movimento. Os dados são estruturados em um formato JSON, conforme exemplificado abaixo:

```cpp
[
    {
        "IdEquipamento": 1,
        "NomeEquipamento": "Lampada Corredor KITNET",
        "AtivacaoSensorMovimento": "false",
        "DtUltimaAlteracao": "2023-10-29 16:56:44.921656",
        "Time": "08:30 AM"
    }
]
```
# Configurando projeto:

Para replicar este projeto, siga as instruções abaixo:

1. Clone o repositório da API:
```bash
git clone https://github.com/BrunoAlbuMaia/APIHome_automation.git
```
2.Configure um ambiente virtual
```bash
python -m venv venv
``` 
Com o ambiente criado, execute o seguinte comando no terminal
```py
venv/bin/activate
```

3. Instale as dependências da API:

```py
pip install -r requirements.txt
```

4. Para executar a api, use o seguinte comando:
```py
python -m main
```

Agora, a API está pronta para ser usada pelo seu projeto de automação residencial baseado em ESP32. Certifique-se de ajustar as configurações do ESP32 para se comunicar com o endereço correto da API, se você ainda não sabe como ajustar a configuração do ESP32 para ele olhar para sua api, [LEIA ESSE SEGUINTE TOPICO](https://github.com/BrunoAlbuMaia/Home_-automation-Esp32-#configura%C3%A7%C3%A3o-do-ambiente-de-desenvolvimento-ide-arduino)



# Operações Principais:

A API oferece endpoints que permitem visualizar, obter detalhes e atualizar o status dos equipamentos no ambiente residencial. As operações principais são:

    Visualizar Equipamentos:
        Endpoint: /VerificandoEquipamentos/
        Método: GET
        Descrição: Retorna uma lista de todos os equipamentos e seus status, indicando se estão ligados ou desligados.

    Obter Dados por ID:
        Endpoint: /ObterDadosPorId/{idEquipamento}
        Método: GET
        Descrição: Retorna os detalhes de um equipamento específico com base no ID fornecido.

    Atualizar Equipamentos:
        Endpoint: /AtualizarEquipamentos/{idEquipamento}
        Método: PATCH
        Descrição: Atualiza os dados de um equipamento específico, como o status de ativação do sensor de movimento, o horário da última alteração, etc.


# Exemplos de Uso:
```cpp
  cd my-project
```
