from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Importando as classes de modelo
from model.base import Base
from model.fatura import Fatura

# Diretório onde o banco de dados será armazenado
db_path = "database/"

# Verifica se o diretório existe; se não existir, cria-o
if not os.path.exists(db_path):
    os.makedirs(db_path)

# URL do banco de dados SQLite
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# Criando um mecanismo de banco de dados SQLAlchemy
engine = create_engine(db_url, echo=False)

# Criando uma classe de sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)

# Verifica se o banco de dados já existe; se não existir, cria-o
if not database_exists(engine.url):
    create_database(engine.url)

# Cria as tabelas no banco de dados com base nos modelos definidos
Base.metadata.create_all(engine)

