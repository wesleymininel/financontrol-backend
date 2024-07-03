from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """
    Esquema Pydantic para representar erros.

    Atributos:
    - message: Mensagem de erro (string).
    """
    message: str