from pydantic import BaseModel

class CursoAluno(BaseModel):
    curso_idCurso: int
    aluno_idAluno: int