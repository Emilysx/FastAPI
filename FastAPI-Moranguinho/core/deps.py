from typing import Generator  # Importando Generator para indicar que a função é um gerador
from sqlalchemy.ext.asyncio import AsyncSession  # Importando AsyncSession para usar sessões assíncronas
from core.database import Session  # Importando a fábrica de sessões do banco

# Função que retorna uma sessão assíncrona
async def get_session() -> Generator:
    session: AsyncSession = Session()  # Cria uma sessão assíncrona
    try:
        yield session  # Retorna a sessão para ser usada nas rotas
    finally:
        await session.close()  # Fecha a sessão após o uso
