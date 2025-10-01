# Para carregar variáveis de ambiente de forma simples
from pydantic.v1 import BaseSettings
#  Para criar a classe base dos models
from sqlalchemy.orm import declarative_base 

# Classe que contém as configurações principais da aplicação
class Settings(BaseSettings):

    # Define o caminho base para a versão 1 da API
    API_V1_STR: str = "/api/v1"

    # URL de conexão com o banco de dados.
    BD_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/moranguinho" # porta que o xampp está usando e o nome do bando

    DBBaseModel = declarative_base()

# Configurações adicionais do Pydantic
class Config: 
    case_sensitive = False # Configuração para não tornar as variáveis de ambiente sensíveis a maiúsculas/minúsculas
    env_file = "env" # Indica onde procurar o arquivo `.env` para as variáveis de ambiente

settings = Settings()