from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from models.personagens_model import Personagem
from schemas.personagem_schema import PersonagemSchema
from core.deps import get_session

router = APIRouter()

# Criar personagem
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonagemSchema)
async def criar_personagem(personagem: PersonagemSchema, db: AsyncSession = Depends(get_session)):
    novo_personagem = Personagem(
        nome=personagem.nome,
        idade=personagem.idade,
        fruta=personagem.fruta,
        descricao=personagem.descricao
    )
    db.add(novo_personagem)
    await db.commit()
    return novo_personagem

# Listar todos os personagens
@router.get("/", response_model=List[PersonagemSchema])
async def listar_personagens(db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(Personagem))
        personagens = result.scalars().all()
        return personagens

# Atualizar personagem
@router.put("/{personagem_id}", response_model=PersonagemSchema)
async def atualizar_personagem(personagem_id: int, personagem: PersonagemSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(Personagem).filter(Personagem.id == personagem_id))
        personagem_db = result.scalars().first()

        if personagem_db:
            personagem_db.nome = personagem.nome
            personagem_db.idade = personagem.idade
            personagem_db.fruta = personagem.fruta
            personagem_db.descricao = personagem.descricao
            await session.commit()
            return personagem_db

        return {"erro": "Personagem não encontrado"}

# Deletar personagem
@router.delete("/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(Personagem).filter(Personagem.id == personagem_id))
        personagem_db = result.scalars().first()

        if personagem_db:
            await session.delete(personagem_db)
            await session.commit()
            return {"msg": "Personagem deletado com sucesso"}

        return {"erro": "Personagem não encontrado"}
