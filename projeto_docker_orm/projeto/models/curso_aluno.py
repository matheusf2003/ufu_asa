from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class CursoAluno(Base):
    __tablename__ = 'cursoAluno'

    id = Column(Integer, primary_key=True)
    curso_idCurso = Column(Integer, ForeignKey('cursos.idCurso'))
    aluno_idAluno = Column(Integer, ForeignKey('alunos.idAluno'))