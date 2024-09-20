from pydantic import BaseModel

class Professor(BaseModel):
    nome: str
    email: str
    cpf: str
    endereco: str
    numero: str
    complemento: str
    cidade: str
    estado: str