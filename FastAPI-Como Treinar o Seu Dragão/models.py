from typing import Optional # significa que o campo é o opcional
from pydantic import BaseModel # para fazer os tipos de dados

class Dragoes(BaseModel):
    id: Optional[int] = None  # O ID será atribuído automaticamente
    nome: str
    especie: str
    idade: int
    nivel: int = 0
    treinador: str
    foto: Optional[str] = None

class Personagens(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    aliado_dragao: Optional[str] = None
    foto: Optional[str] = None