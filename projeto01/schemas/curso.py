from pydantic import BaseModel

class CursoSchema(BaseModel):
    nome: str
    carga_horaria: int
    periodo: int
    descricao: str