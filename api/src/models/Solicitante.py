from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Solicitante(db.Model):

    codigo_solicitante : Mapped[int] = mapped_column(primary_key=True,unique=True)
    profissional_solicitante : Mapped[str] = mapped_column(String(70))
    conselho_profissional : Mapped[int]
    numero_conselho_profissional : Mapped[str] = mapped_column(String(15))
    uf : Mapped[int]
    cbos : Mapped[int]
    execucao_spsadt : Mapped[List["ExecucaoSPSADT"]] = relationship(back_populates="solicitante")