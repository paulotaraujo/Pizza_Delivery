from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Esta e a rota padrao de autenticacao do nosso sistema.
    """
    return {"mensagem":"Voce acessou a rota de autenticacao", "autenticado": False}
