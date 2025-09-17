# Arquivo do Bnacod e dados
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.BD_URL)

Session:  AsyncEngine = sessionmaker(
    autocommit = False,
    autoflush = False,
    expire_ = AsyncSession,
    bind = engine
)














