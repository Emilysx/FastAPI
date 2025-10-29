from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from models.aventura_model import Aventura
from schemas.aventura_schema import AventuraSchema
from core.deps import get_session

router = APIRouter()

# Criar aventura
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AventuraSchema)
async def criar_aventura(aventura: AventuraSchema, db: AsyncSession = Depends(get_session)):
    nova_aventura = Aventura(
        nome=aventura.nome,
        descricao=aventura.descricao,
        personagem_id=aventura.personagem_id
    )
    db.add(nova_aventura)
    await db.commit()
    return nova_aventura

# Listar aventuras
@router.get("/", response_model=List[AventuraSchema])
async def listar_aventuras(db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(Aventura))
        aventuras = result.scalars().all()
        return aventuras

# Atualizar aventura
@router.put("/{aventura_id}", response_model=AventuraSchema)
async def atualizar_aventura(aventura_id: int, aventura: AventuraSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(Aventura).filter(Aventura.id == aventura_id))
        aventura_db = result.scalars().first()

        if aventura_db:
            aventura_db.nome = aventura.nome
            aventura_db.descricao = aventura.descricao
            aventura_db.personagem_id = aventura.personagem_id
            await session.commit()
            return aventura_db

        return {"erro": "Aventura não encontrada"}

# Deletar aventura
@router.delete("/{aventura_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_aventura(aventura_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(Aventura).filter(Aventura.id == aventura_id))
        aventura_db = result.scalars().first()

        if aventura_db:
            await session.delete(aventura_db)
            await session.commit()
            return {"msg": "Aventura deletada com sucesso"}

        return {"erro": "Aventura não encontrada"}

