from fastapi          import APIRouter, Depends, HTTPException, Response, status
from models.curso    import Curso
from schemas.curso   import CursoSchema
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

@router.get("/curso")
async def root():
    return {"mensagem": "Dentro de curso"}    


@router.post("/curso")
def cria_curso(curso: CursoSchema, db: Session = Depends(get_db)):
    novo_curso = Curso(**curso.model_dump())
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso

@router.get("/curso")
def get(db: Session = Depends(get_db)):
    todos_cursos = db.query(Curso).all()
    return todos_cursos

@router.delete("/curso/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Curso).filter(Curso.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/Curso/{id}")
def update(id: int, curso:CursoSchema, db:Session = Depends(get_db)):
    updated_post = db.query(Curso).filter(Curso.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso: {id} does not exist')
    else:
        updated_post.update(curso.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()

