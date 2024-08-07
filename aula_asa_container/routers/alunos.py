from fastapi import APIRouter, Depends
from schemas.alunos import Aluno

router = APIRouter()

@router.get("/alunos/{aluno_id}")
async def root():
    return {"message": "Dentro de alunos"}

@router.get("/alunos/{aluno_id}")
async def criar_aluno(aluno:Aluno):
    return {"message": "Aluno criado com sucesso!"}