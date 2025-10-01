from core.configs import settings  # configurações, como a base do banco de dados
from core.database import engine 
from models import __all_models  # Importa todos os modelos para garantir que sejam registrados

# Função assíncrona para criar as tabelas
async def create_tables() -> None:
    print("Criando tabelas no banco de dados...")

    # Usando a conexão assíncrona para iniciar a criação das tabelas
    async with engine.begin() as conn:
        # Apaga as tabelas existentes, se houver
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        
        # Cria todas as tabelas definidas nos modelos
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)

    print("Tabelas criadas com sucesso!")

# Execução do script assíncrono
if __name__ == "__main__":
    import asyncio

    # Executa a função assíncrona de criação das tabelas
    asyncio.run(create_tables())  
