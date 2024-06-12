from fastapi          import APIRouter, Depends, HTTPException, Response, status
from models.alunos    import Alunos
from schemas.alunos   import AlunosSchema
from sqlalchemy.orm   import Session
from models.database  import get_db
import logging
import coloredlogs, logging

router = APIRouter()


log_colors = {
    'DEBUG': 'cyan',
    'INFO': 'light_white',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
coloredlogs.install()

@router.get("/alunos")
async def root():
    return {"mensagem": "Dentro de alunos"}    

@router.get("/teste_logs")
async def teste_logs():    
    logging.info('This is an info message')
    #logging.error('%s raised an error', name)   
    logging.error('%s raised an error', 'MARCIO')   


@router.post("/alunos")
def cria_alunos(aluno: AlunosSchema, db: Session = Depends(get_db)):
    novo_aluno = Alunos(**aluno.model_dump())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

@router.get("/alunos")
def get(db: Session = Depends(get_db)):
    todos_alunos = db.query(Alunos).all()
    return todos_alunos

@router.delete("/alunos/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Alunos).filter(Alunos.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Aluno não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/alunos/{id}")
def update(id: int, aluno:AlunosSchema, db:Session = Depends(get_db)):
    updated_post = db.query(Alunos).filter(Alunos.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno: {id} does not exist')
    else:
        updated_post.update(aluno.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()

