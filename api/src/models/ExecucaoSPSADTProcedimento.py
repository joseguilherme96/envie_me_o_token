from __future__ import annotations
from typing import TYPE_CHECKING
from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

if TYPE_CHECKING:
    from .ExecucaoSPSADT import ExecucaoSPSADT


class ExecucaoSPSADTProcedimento(db.Model):
    codigo_execucao_procedimento: Mapped[int] = mapped_column(
        primary_key=True,
        comment="Chave primária da tabela.",
        unique=True,
        autoincrement=True,
    )
    codigo_procedimento: Mapped[int] = mapped_column(comment="Ver na guia do paciente.")
    codigo_execucao: Mapped[int] = mapped_column(
        ForeignKey("execucao_spsadt.codigo_execucao")
    )
    execucao_spsadt: Mapped["ExecucaoSPSADT"] = relationship(
        back_populates="execucao_spsadt_procedimento"
    )
    descricao_procedimento: Mapped[str] = mapped_column(
        String(150), comment="Ver na guia do paciente."
    )
    quantidade_solicitada: Mapped[int]

    def inserir(procedimento):
        try:
            db.session.begin()
            db.session.add(procedimento)
            db.session.commit()
            return {
                "codigo_execucao_procedimento": procedimento.codigo_execucao_procedimento,
                "codigo_procedimento": procedimento.codigo_procedimento,
                "codigo_execucao": procedimento.codigo_execucao,
                "descricao_procedimento": procedimento.descricao_procedimento,
                "quantidade_solicitada": procedimento.quantidade_solicitada,
            }
        except Exception:
            db.session.rollback()
            raise
