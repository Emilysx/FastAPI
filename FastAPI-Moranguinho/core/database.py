from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings  # As configurações (URL do banco)

# Conexão com o banco de dados usando a URL configurada
engine: AsyncEngine = create_async_engine(settings.BD_URL)  

# Criando a fábrica de sessões assíncronas (sessionmaker) com a engine
Session: AsyncEngine = sessionmaker(
    autocommit=False,  # Desativa o autocommit, transações devem ser feitas manualmente
    autoflush=False,   # Desativa o autoflush, dados não são atualizados automaticamente
    expire_on_commit=False,  # Não expira os objetos após o commit
    class_=AsyncSession,  # Usando a classe assíncrona para a sessão
    bind=engine  # Associando a engine à sessão
)