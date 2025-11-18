from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer,ForeignKey,Text

class ExecucaoSPSADT(db.Model):

    codigo_execucao : Mapped[int] = mapped_column(primary_key=True,unique=True)
    codigo_beneficiario : Mapped[str] = mapped_column(ForeignKey("beneficiario.numero_carteira"))
    beneficiario : Mapped["Beneficiario"] = relationship(back_populates="execucao_spsadt")
    codigo_contratado : Mapped[int] = mapped_column(ForeignKey("contratado.codigo_prestador_na_operadora"))
    contratado : Mapped["Contratado"] = relationship(back_populates="execucao_spsadt")
    codigo_solicitante : Mapped[int] = mapped_column(ForeignKey("solicitante.codigo_solicitante"))
    solicitante : Mapped["Solicitante"] = relationship(back_populates="execucao_spsadt")
    operadora_registro_ans : Mapped[int] = mapped_column(ForeignKey("operadora.registro_ans"))
    operadora: Mapped["Operadora"] = relationship(back_populates="execucao_spsadt")
    login : Mapped[str] = mapped_column(ForeignKey("users.login"))
    users : Mapped["Users"] = relationship(back_populates="execucao_spsadt")
    indicacao_clinica : Mapped[bool]
    indicacao_acidente : Mapped[int] = mapped_column(comment="Ver tiss/schema.")
    observacao : Mapped[Text] = mapped_column(Text(length=500))
    senha : Mapped[str] = mapped_column(String(20))
    tipo_transacao : Mapped[str] = mapped_column(String(30))
    transacao: Mapped[list["Transacao"]] = relationship(back_populates="execucao_spsadt")
    execucao_spsadt_procedimento : Mapped[List["ExecucaoSPSADTProcedimento"]] = relationship(back_populates="execucao_spsadt")