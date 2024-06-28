from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from model.fatura import Fatura




class FaturaSchema(BaseModel):
    """ Define como uma nova fatura sera inserida e representada
    """
    beneficiario: str = "Sabesp"
    valor: float = 150.80
    pagador: str = "Wesley"
    vencimento: date = "2024-07-10"




class FaturaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca que sera
        feita apenas com base no beneficiario do fatura.
    """
    beneficiario: str = "Sabesp"


class ListagemFaturasSchema(BaseModel):
    """ Define como uma listagem de faturas sera retornada.
    """
    faturas:List[FaturaSchema]


def apresenta_faturas(faturas: List[Fatura]):
    """ Retorna uma representação da fatura seguindo o schema definido em
        FaturaViewSchema.
    """
    result = []
    for fatura in faturas:
        result.append({
            "beneficiario": fatura.beneficiario,
            "valor": fatura.valor,
            "pagador": fatura.pagador,
            "vencimento": fatura.vencimento
        })

    return {"faturas": result}


class FaturaViewSchema(BaseModel):
    """ Define como uma fatura sera retornada
    """
    beneficiario: str = "Sabesp"
    valor: float = 150.80
    pagador: str = "Wesley"
    vencimento: date = "2024-07-10"



class FaturaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado apos uma requisição
        de remocao.
    """
    mesage: str
    beneficiario: str

def apresenta_fatura(fatura: Fatura):
    """ Retorna uma representação da fatura seguindo o schema definido em
        FaturaViewSchema.
    """
    return {
        "beneficiario": fatura.beneficiario,
        "valor": fatura.valor,
        "pagador": fatura.pagador,
        "vencimento": fatura.vencimento,
     }
