from fastapi import FastAPI
from typing import Optional
from routers.alunos import router as router_alunos
from routers.curso import router as router_curso
from routers.curso_aluno import router as router_cursoAluno
from routers.professor import router as router_professor
from models.database import engine
from models.alunos import Alunos
from models.alunos import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_alunos)
app.include_router(router_curso)
app.include_router(router_cursoAluno)
app.include_router(router_professor)