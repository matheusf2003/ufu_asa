from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Alunos(Base):
    __tablename__ = 'alunos'

    idAluno = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    cpf = Column(String(45), nullable=False)
    endereco = Column(String(45))
    numero = Column(Integer)
    complemento = Column(String(45))
    cidade = Column(String(45))
    estado = Column(String(45))