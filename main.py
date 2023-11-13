from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.homeController import router as home
from src.controllers.hidroController import router as hidro

app = FastAPI(title="HomeAutomationAPI",
              description="Api de comunicacao com automocao residencial. "
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Adicionando as rotas ao aplicativo
app.include_router(home, prefix="/home")
app.include_router(hidro, prefix="/hidro")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9001)