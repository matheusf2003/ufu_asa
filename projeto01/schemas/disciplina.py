from pydantic import BaseModel

class DisciplinaSchema(BaseModel):
    descricao: str
    codigo: str
    creditos: int