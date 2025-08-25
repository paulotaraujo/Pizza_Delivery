from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Esta e a rota padrao de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de autenticacao.
    """
    return {"mensagem":"Voce acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedidoSchema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(pedidoSchema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso! ID do pedido: {novo_pedido.id}"}