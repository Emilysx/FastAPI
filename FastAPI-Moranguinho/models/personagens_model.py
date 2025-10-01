from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import DBBaseModel  # BaseModel para herdar os recursos do SQLAlchemy

class Personagem(DBBaseModel):
    __tablename__ = 'personagens'  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)  # Chave primária para identificar o personagem
    nome = Column(String, index=True)  
    idade = Column(Integer) 
    fruta = Column (String)
    descricao = Column(String)

    # Relacionamento com a tabela de Aventuras (um personagem pode participar de várias aventuras)
    aventuras = relationship("Aventura", back_populates="personagem")
