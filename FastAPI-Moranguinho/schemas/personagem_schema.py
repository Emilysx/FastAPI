# personagem_schema.py
from typing import Optional
from pydantic import BaseModel as SCBasModel

class PersonagemSchema(SCBasModel):
    # Campos do personagem
    id: Optional[int] = None  
    nome: str  
    idade: int  
    fruta: str
    descricao: str  

    class Config:
        orm_mode = True  # Permite que o Pydantic converta os dados do ORM (SQLAlchemy) para o formato JSON
