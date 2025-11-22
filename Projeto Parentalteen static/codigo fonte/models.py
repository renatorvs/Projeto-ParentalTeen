from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    telefone = Column(String)
    data_nascimento = Column(Date)