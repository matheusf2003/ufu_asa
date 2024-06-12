from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.disciplina import Disciplina
from schemas.disciplina import DisciplinaSchema
from sqlalchemy.orm import Session
from models.database import get_db
import logging
import coloredlogs

router = APIRouter()

@router.get("/disciplina")
async def root():
    return {"mensagem": "Dentro de disciplina"}



@router.post("/disciplina")
def cria_disciplina(disciplina: DisciplinaSchema, db: Session = Depends(get_db)):
    nova_disciplina = Disciplina(**disciplina.model_dump())
    db.add(nova_disciplina)
    db.commit()
    db.refresh(nova_disciplina)
    return nova_disciplina

@router.get("/disciplina")
def get(db: Session = Depends(get_db)):
    todas_disciplinas = db.query(Disciplina).all()
    return todas_disciplinas

@router.delete("/disciplina/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Disciplina).filter(Disciplina.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Disciplina não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/disciplina/{id}")
def update(id: int, disciplina:DisciplinaSchema, db:Session = Depends(get_db)):
    updated_post = db.query(Disciplina).filter(Disciplina.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Disciplina: {id} does not exist')
    else:
        updated_post.update(disciplina.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()