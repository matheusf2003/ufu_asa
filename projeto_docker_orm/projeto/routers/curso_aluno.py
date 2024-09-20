from fastapi          import APIRouter, Depends, HTTPException, Response, status
from schemas.curso_aluno import CursoAluno
from models.database  import get_db
from models.curso_aluno import CursoAluno as CursoAlunoModel
from sqlalchemy.orm   import Session

router = APIRouter()

@router.get("/curso_aluno")
def get(db: Session = Depends(get_db)):
    all_curso_aluno = db.query(CursoAlunoModel).all()
    return all_curso_aluno


@router.post("/curso_aluno")
async def criar_curso_aluno(curso_aluno: CursoAluno, db: Session = Depends(get_db)):
    novo_curso_aluno = CursoAlunoModel(**curso_aluno.model_dump())
    try:
        db.add(novo_curso_aluno)
        db.commit()
        db.refresh(novo_curso_aluno)
        return { "mensagem": "CursoAluno criado com sucesso",
                 "novo_curso_aluno": novo_curso_aluno}
    except Exception as e:
            print(e)
            return { "mensagem": "Problemas para inserir o CursoAluno",
                 "novo_curso_aluno": novo_curso_aluno}

@router.delete("/curso_aluno/{id}")
def delete(id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT):
    delete_post = db.query(CursoAlunoModel).filter(CursoAlunoModel.id == id)
    
    if delete_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"CursoAluno não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   


@router.put("/curso_aluno/{id}")
def update(id: int, curso: CursoAluno, db: Session = Depends(get_db)):
    updated_post = db.query(CursoAlunoModel).filter(CursoAlunoModel.id == id)
    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'CursoAluno: {id} does not exist')
    else:
        updated_post.update(curso.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()