from fastapi import FastAPI, HTTPException, Depends,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.get("/")
def index():
    return{"mensagem":"Olá mundo!"}

# Por no cmd uvicorn main:app --reload
# Para parar de rodar da um ctrlC

@app.post("/token")
async def logar(data: OAuth2PasswordRequestForm = Depends()):
    if data.username == "Alana" and data.password == "senai123":
        return {"acces_token": "supersecreto","token_type":"bearer"}
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Credencias Inválidas")

# bearer tipo de token, raise faz levantamento de erros