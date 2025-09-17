from core.configs import settings
from sqlalchemy import Colunm, Integer, String, Float, Boolean

class BandasModel(settings.DBBaseModel):
    __tablename__ = "bandas"

    id: int = Colunm(Integer(), primary_key=True, autoincrement=True)
    nome: str = Colunm(String(256))
    qtd_integrantes: int = (Integer())
    tipo_musical: str = Colunm(String(256))


