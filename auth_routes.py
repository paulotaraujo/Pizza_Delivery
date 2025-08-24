from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Esta e a rota padrao de autenticacao do nosso sistema.
    """
    return {"mensagem":"Voce acessou a rota de autenticacao", "autenticado": False}

@auth_router.post("/criar_conta")
async def crair_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    
    if usuario:
        return{"mensagem":"ja existe um usuario com esse email"}
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":"usuario cadastrado com sucesso!"}
