from fastapi          import APIRouter, Depends, HTTPException, Response, status
from schemas.professores   import Professor
from models.database  import get_db
from models.professores    import Professores
from sqlalchemy.orm   import Session
import logging


router = APIRouter()

@router.get("/professores")
def get(db: Session = Depends(get_db)):
    all_professores = db.query(Professores).all()
    logging.info("GET_ALL_PROFESSORES")
    professores = []
    for professor in all_professores:
        item = {"id": professor.idProfessor,
                "nome": professor.nome}
        professores.append(item)       
    logging.info(professores)
    return all_professores

@router.post("/professores")
async def criar_professor(professor: Professor, db: Session = Depends(get_db)):
    novo_professor = Professores(**professor.model_dump())
    db.add(novo_professor)
    db.commit()
    db.refresh(novo_professor)
    return { "mensagem": "Professor criado com sucesso",
             "professor": novo_professor 
    }


@router.delete("/professores/{id}")
def delete_professor(id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    delete_professor = db.query(Professores).filter(Professores.idProfessor == id)
    
    if delete_professor.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor não existe")
    else:
        delete_professor.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/professores/{id}")
def update_professor(id: int, professor: Professor, db: Session = Depends(get_db)):
    updated_professor = db.query(Professores).filter(Professores.idProfessor == id)
    
    if updated_professor.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor não existe")
    else:
        updated_professor.update(professor.model_dump(), synchronize_session=False)
        db.commit()
    return {"mensagem": "Professor atualizado com sucesso"}