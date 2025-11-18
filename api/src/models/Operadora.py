
from __future__ import annotations
from .db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Operadora(db.Model):

    registro_ans : Mapped[int] = mapped_column(unique=True,primary_key=True,comment="Nº de registro da operadora na ANS.")
    operadora : Mapped[str] = mapped_column(String(30),comment="Nome da operadora")
    execucao_spsadt : Mapped[list[ExecucaoSPSADT]] = relationship(back_populates="operadora")