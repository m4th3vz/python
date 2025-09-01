'''
CRUD completo de clientes usando SQLAlchemy ORM com banco SQLite.

Funcionalidades:
- Criação do banco "meu_banco.sqlite" na mesma pasta do script.
- Criação da tabela 'clientes' se não existir.
- Inserção de clientes de exemplo caso o banco esteja vazio.
- Operações CRUD:
    - Create: adicionar clientes (individual ou múltiplos)
    - Read: listar todos ou consultar por ID
    - Update: atualizar dados de um cliente
    - Delete: remover cliente pelo ID
- Listagem final para verificar alterações.
- Mensagem de boas-vindas para cliente recuperado por ID.

Boas práticas:
- ORM elimina necessidade de SQL manual.
- Banco criado automaticamente no diretório do script.
- Session gerencia transações e commits.
- Código legível, organizado e portátil.

Ideal para estudo de SQL e integração com Python usando ORM.
'''

from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# --- Configuração do caminho do banco ---
ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / "meu_banco_orm.sqlite"

# --- Criação do engine (banco dentro da pasta do script) ---
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# --- Classe que representa a tabela 'clientes' ---
class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(150))

# --- Cria a tabela se não existir ---
Base.metadata.create_all(engine)

# --- Inserção de clientes de exemplo se tabela estiver vazia ---
if session.query(Cliente).count() == 0:
    clientes_exemplo = [
        Cliente(nome="Guilherme", email="guilherme@gmail.com"),
        Cliente(nome="Chappie", email="chappie@gmail.com"),
        Cliente(nome="Melaine", email="melaine@gmail.com"),
    ]
    session.add_all(clientes_exemplo)
    session.commit()
    print("Clientes de exemplo inseridos.\n")

# --- CRUD completo ---

# Listar todos os clientes
print("Lista de todos os clientes:")
todos = session.query(Cliente).order_by(Cliente.nome.desc()).all()
for c in todos:
    print(c.id, c.nome, c.email)
print()

# Recuperar cliente específico
cliente = session.query(Cliente).filter_by(id=2).first()
if cliente:
    print("Cliente com ID 2:")
    print(cliente.id, cliente.nome, cliente.email)
    print(f"Seja bem-vindo ao sistema {cliente.nome}\n")
else:
    print("Cliente com ID 2 não encontrado.\n")

# Exemplo de Update
if cliente:
    cliente.nome = "Guilherme Silva"
    session.commit()
    print(f"Nome do cliente ID 2 atualizado para: {cliente.nome}\n")

# Exemplo de Delete
if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente ID 2 removido.\n")

# Listagem final para confirmar alterações
print("Lista final de clientes:")
for c in session.query(Cliente).order_by(Cliente.nome.desc()).all():
    print(c.id, c.nome, c.email)

# --- Fechar sessão ---
session.close()
