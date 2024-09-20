from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Professores(Base):
    __tablename__ = 'professores'

    idProfessor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(20), nullable=False)
    cpf = Column(String(45))
    endereco = Column(String(45))
    numero = Column(String(45))
    complemento = Column(String(45))
    cidade = Column(String(45))
    estado = Column(String(45))