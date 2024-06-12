from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.departamento import Departamento
from schemas.departamento import DepartamentoSchema
from sqlalchemy.orm import Session
from models.database import get_db
import logging
import coloredlogs

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

@router.get("/departamento")
async def root():
    return {"mensagem": "Dentro de departamento"}


@router.post("/departamento")
def cria_departamento(departamento: DepartamentoSchema, db: Session = Depends(get_db)):
    novo_departamento = Departamento(**departamento.model_dump())
    db.add(novo_departamento)
    db.commit()
    db.refresh(novo_departamento)
    return novo_departamento

@router.get("/departamento")
def get(db: Session = Depends(get_db)):
    todos_departamentos = db.query(Departamento).all()
    return todos_departamentos

@router.delete("/departamento/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Departamento).filter(Departamento.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Departamento não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/departamento/{id}")
def update(id: int, departamento:DepartamentoSchema, db:Session = Depends(get_db)):
    updated_post = db.query(Departamento).filter(Departamento.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Departamento: {id} does not exist')
    else:
        updated_post.update(departamento.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()

