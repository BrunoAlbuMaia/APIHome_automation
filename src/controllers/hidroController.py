from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from src.services.DadosHidroService import GestorHidroJSON
from datetime import datetime

router = APIRouter()

@router.get("/PorcentagemCaixa/", tags=['hidro'], summary="Mostra a porcentagem que a caixa de agua esta ocupando")
async def verificaEquipamentos():
    dadosJson = GestorHidroJSON("src/data/dadoHidro.json")
    dadosJson.ler_dados_json()
    return JSONResponse(content=dadosJson.ler_dados_json())
    

@router.patch("/ValorMedido/{valorcm}",tags=["hidro"],summary="Aqui e onde e passado o valor em cm, que e medido pelo Sensor Ultrassonico")
async def valorMedido(valorcm:int):
    dadosJson = GestorHidroJSON("src/data/dadoHidro.json")
    dadosJson.ler_dados_json()
    dadosJson.atualizar_dados(1,valorcm)
    resultado = dadosJson.ler_dados_json()
    return JSONResponse(content=resultado)