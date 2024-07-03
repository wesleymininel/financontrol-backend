from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Fatura
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API - Controle Financeiro Mensal", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
fatura_tag = Tag(name="Fatura", description="Adição, visualização e remocao de faturas na base")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/listfaturas', tags=[fatura_tag],
         responses={"200": ListagemFaturasSchema, "404": ErrorSchema})
def get_faturas():
    """Faz a busca por todas as Fatura cadastradas

    Retorna uma representação da listagem de faturas.
    """
    logger.debug(f"Coletando faturas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    faturas = session.query(Fatura).all()

    if not faturas:
        # se não há faturas cadastradas
        return {"faturas": []}, 200
    else:
        logger.debug(f"%d faturas encontradas" % len(faturas))
        # retorna a representação da fatura
        print(faturas)
        return apresenta_faturas(faturas), 200


@app.delete('/delfatura', tags=[fatura_tag],
            responses={"200": FaturaDelSchema, "404": ErrorSchema})
def del_fatura(query: FaturaBuscaSchema):
    """Deleta uma Fatura a partir do beneficiario da fatura informada

    Retorna uma mensagem de confirmação da remoção.
    """
    fatura_beneficiario = unquote(unquote(query.beneficiario))
    print(fatura_beneficiario)
    logger.debug(f"Deletando dados sobre fatura #{fatura_beneficiario}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Fatura).filter(Fatura.beneficiario == fatura_beneficiario).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado fatura #{fatura_beneficiario}")
        return {"mesage": "Fatura removida", "beneficiario": fatura_beneficiario}
    else:
        # se a fatura não foi encontrado
        error_msg = "Fatura não encontrada na base"
        logger.warning(f"Erro ao deletar fatura #'{fatura_beneficiario}', {error_msg}")
        return {"mesage": error_msg}, 404

    # retorna a representação da fatura
    return apresenta_fatura(fatura), 200


@app.get('/findfatura', tags=[fatura_tag],
         responses={"200": FaturaViewSchema, "404": ErrorSchema})
def get_fatura(query: FaturaBuscaSchema):
    """Faz a busca por uma Fatura a partir do beneficiario da fatura

    """
    fatura_beneficiario = query.beneficiario
    logger.debug(f"Coletando dados sobre fatura #{fatura_beneficiario}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    fatura = session.query(Fatura).filter(Fatura.beneficiario == fatura_beneficiario).first()

    if not fatura:
        # se a fatura não foi encontrada
        error_msg = "Fatura não encontrada"
        logger.warning(f"Erro ao buscar fatura '{fatura_beneficiario}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Fatura econtrada: '{fatura.beneficiario}'")
        # retorna a representação da fatura
        return apresenta_fatura(fatura), 200


@app.post('/addfatura', tags=[fatura_tag],
          responses={"200": FaturaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_fatura(form: FaturaSchema):
    """Adiciona uma nova Fatura à base de dados

    """
    fatura = Fatura(
        beneficiario=form.beneficiario,
        valor=form.valor,
        pagador=form.pagador,
        vencimento=form.vencimento)
    logger.debug(f"Adicionando fatura de beneficiario: '{fatura.beneficiario}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando fatura
        session.add(fatura)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado fatura de beneficiario: '{fatura.beneficiario}'")
        return apresenta_fatura(fatura), 200

    except IntegrityError as e:
        # como a duplicidade do beneficiario é a provável razão do IntegrityError
        error_msg = "Fatura de mesmo beneficiario já salvo na base"
        logger.warning(f"Erro ao adicionar fatura '{fatura.beneficiario}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item"
        logger.warning(f"Erro ao adicionar fatura '{fatura.beneficiario}', {error_msg}")
        return {"mesage": error_msg}, 400

