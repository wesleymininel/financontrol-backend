from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Fatura(Base):
    __tablename__ = 'fatura'

    id = Column("pk_fatura", Integer, primary_key=True)
    beneficiario = Column(String(140))
    valor = Column(Float)
    pagador = Column(String(140))
    vencimento = Column(DateTime)
    data_insercao = Column(DateTime, default=datetime.now())



    def __init__(self, beneficiario:str, valor:float, pagador:str, vencimento:DateTime,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Fatura

        Arguments:
            beneficiario: beneficiario da fatura.
            valor: valor esperado da fatura
            pagador: pagador da fatura
            vencimento: Data de vencimento da fatura
            data_insercao: data de quando a fatura foi inserido à base
        """
        self.beneficiario = beneficiario
        self.valor = valor
        self.pagador = pagador
        self.vencimento = vencimento

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao



