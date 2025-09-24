from typing import Optional
from pydantic import BaseModel as SCBasModel

class BandasSchema(SCBasModel):

    id: Optional[int] = None
    nome: str
    qtd_integrantes: int
    tipo_musical: str

    class Config:
        orm_mode = True










