from fastapi          import APIRouter, Depends, HTTPException, Response, status
from schemas.cursos   import Curso
from models.database  import get_db
from models.cursos    import Cursos
from sqlalchemy.orm   import Session

router = APIRouter()

@router.get("/cursos")
def get(db: Session = Depends(get_db)):
    all_cursos = db.query(Cursos).all()
    return all_cursos


@router.post("/cursos")
async def criar_cursos(curso: Curso, db: Session = Depends(get_db)):
    novo_curso = Cursos(**curso.model_dump())
    try:
        db.add(novo_curso)
        db.commit()
        db.refresh(novo_curso)
        return { "mensagem": "Curso criado com sucesso",
                 "novo_curso": novo_curso}
    except Exception as e:
            print(e)
            return { "mensagem": "Problemas para inserir o curso",
                 "novo_curso": novo_curso}

 
@router.delete("/cursos/{id}")
def delete(id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Cursos).filter(Cursos.idCurso == id)
    
    if delete_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   


@router.put("/cursos/{id}")
def update(id: int, curso: Curso, db: Session = Depends(get_db)):
    updated_post = db.query(Cursos).filter(Cursos.idCurso == id)
    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso: {id} does not exist')
    else:
        updated_post.update(curso.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()
