
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/parentalteen"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    telefone = Column(String)
    data_nascimento = Column(Date)
    desafio = Column(String)
    criado_em = Column(Date, nullable=False, server_default="now()")

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")
