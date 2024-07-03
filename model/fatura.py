from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base  # Importa a classe Base para definir a herança do SQLAlchemy

class Fatura(Base):
    __tablename__ = 'fatura'  # Nome da tabela no banco de dados

    id = Column("pk_fatura", Integer, primary_key=True)  # Coluna de chave primária
    beneficiario = Column(String(140))  # Coluna para o nome do beneficiário (máximo de 140 caracteres)
    valor = Column(Float)  # Coluna para o valor da fatura
    pagador = Column(String(140))  # Coluna para o nome do pagador (máximo de 140 caracteres)
    vencimento = Column(DateTime)  # Coluna para a data de vencimento da fatura
    data_insercao = Column(DateTime, default=datetime.now())  # Coluna para a data de inserção, com valor padrão definido como o momento atual

    def __init__(self, beneficiario: str, valor: float, pagador: str, vencimento: DateTime,
                 data_insercao: Union[DateTime, None] = None):
        """
        Construtor da classe Fatura.

        beneficiario: Nome do beneficiário da fatura.
        valor: Valor da fatura.
        pagador: Nome do pagador da fatura.
        vencimento: Data de vencimento da fatura.
        data_insercao: Data de inserção da fatura (opcional).
        """
        self.beneficiario = beneficiario
        self.valor = valor
        self.pagador = pagador
        self.vencimento = vencimento

        if data_insercao:
            self.data_insercao = data_insercao
