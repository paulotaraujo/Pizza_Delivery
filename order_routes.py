from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Esta e a rota padrao de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de autenticacao.
    """
    return {"mensagem":"Voce acessou a rota de pedidos"}