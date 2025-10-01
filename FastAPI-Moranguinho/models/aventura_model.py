from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import DBBaseModel  # BaseModel para herdar os recursos do SQLAlchemy

class Aventura(DBBaseModel):
    __tablename__ = 'aventuras'  # Nome da tabela de Aventuras

    id = Column(Integer, primary_key=True, index=True)  # Chave primária para identificar a aventura
    nome = Column(String, index=True) 
    descricao = Column(String) 

    # Relacionamento com a tabela de Personagens (um personagem pode participar de várias aventuras)
    personagem_id = Column(Integer, ForeignKey('personagens.id'))  # Chave estrangeira para vincular ao personagem
    personagem = relationship("Personagem", back_populates="aventuras")  # Relacionamento bidirecional
