from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from src.services.ManipuladorJSONService import GestorDeDadosJSON
from datetime import datetime

router = APIRouter()

@router.get("/VerificandoEquipamentos/", tags=['home'], summary="Mostra todos os equipamentos e os status deles, se ta desligado e etc")
async def verificaEquipamentos():
    dadosJson = GestorDeDadosJSON("src/data/dados.json")
    dadosJson.ler_dados_json()
    return JSONResponse(content=dadosJson.ler_dados_json())

@router.get("/ObterDadosPorId/{idEquipamento}",tags=["home"],summary="") 
async def obterdadosId(idEquipamento:int):
    dadosJson = GestorDeDadosJSON("src/data/dados.json")
    dadosJson.ler_dados_json()
    return dadosJson.obter_dados_por_id(idEquipamento)
    
@router.patch("/AtualizarEquipamentos/{idEquipamento}",tags=['home'],summary="Atualiza os dados de um determinado equipamentos")
async def atualizarDados(idEquipamento:int, dados:dict):
    data_hora_atual = datetime.now()
    dados["DtUltimaAlteracao"] = f"{data_hora_atual}"
    
    dadosJson = GestorDeDadosJSON("src/data/dados.json")
    dadosJson.ler_dados_json()
    await dadosJson.atualizar_dados(1,dados)
    
    resultado = dadosJson.ler_dados_json()
    
    return JSONResponse(content=resultado)
    

