from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    email: str
    cpf: str
    endereco: str
    numero: int
    complemento: str
    cidade: str
    estado: str
