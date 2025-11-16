from db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Operadora(db.model):

    registro_ans : Mapped[int] = mapped_column(unique=True,primary_key=True,comment="Nº de registro da operadora na ANS.")
    operadora : Mapped[str] = mapped_column(String(30),comment="Nome da operadora")