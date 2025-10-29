# aventura_schema.py
from typing import Optional
from pydantic import BaseModel as SCBasModel

class AventuraSchema(SCBasModel):
    # Campos da aventura
    id: Optional[int] = None  
    nome: str  
    descricao: str  

    # Definindo a chave estrangeira para vincular ao personagem
    personagem_id: Optional[int] = None  # Este campo será a chave estrangeira

    class Config:
        orm_mode = True  # Permite que o Pydantic converta os dados do ORM (SQLAlchemy) para JSON
