from __future__ import annotations
from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer,ForeignKey



class ExecucaoSPSADTProcedimento(db.Model):

    codigo_procedimento : Mapped[int] = mapped_column(comment="Ver na guia do paciente.",primary_key=True)
    codigo_execucao : Mapped[int] = mapped_column(ForeignKey("execucao_spsadt.codigo_execucao"))
    execucao_spsadt : Mapped["ExecucaoSPSADT"] = relationship(back_populates="execucao_spsadt_procedimento")
    descricao_procedimento : Mapped[str] = mapped_column(String(150),comment="Ver na guia do paciente.")
    quantidade_solicitada : Mapped[int]