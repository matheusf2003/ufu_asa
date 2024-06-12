from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Disciplina(Base):
    __tablename__ = 'disciplina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50), nullable=False)
    codigo = Column(String(20), nullable=False)
    creditos = Column(Integer, nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    depto_id = Column(Integer, ForeignKey('departamento.id'))
