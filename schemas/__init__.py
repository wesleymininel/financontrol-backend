from schemas.fatura import (
    FaturaSchema,            # Esquema para serialização de uma fatura
    FaturaBuscaSchema,       # Esquema para serialização de busca de fatura
    FaturaViewSchema,        # Esquema para serialização de visualização de fatura
    ListagemFaturasSchema,   # Esquema para serialização de lista de faturas
    FaturaDelSchema,         # Esquema para serialização de exclusão de fatura
    apresenta_faturas,       # Função para apresentar múltiplas faturas
    apresenta_fatura         # Função para apresentar uma fatura específica
)
from schemas.error import ErrorSchema  # Esquema para serialização de erros

