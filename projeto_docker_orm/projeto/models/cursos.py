from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Cursos(Base):
    __tablename__ = 'cursos'

    idCurso = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    idProfessor = Column(Integer, ForeignKey('professores.idProfessor'))