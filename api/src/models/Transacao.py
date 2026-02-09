from __future__ import annotations
from typing import List, TYPE_CHECKING
from .db import db
from sqlalchemy import ForeignKey, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .ExecucaoSPSADT import ExecucaoSPSADT
    from .TransacaoStatus import TransacaoStatus


class Transacao(db.Model):
    sequencia_transacao: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True
    )
    codigo_execucao_sp_sadt: Mapped[int] = mapped_column(
        ForeignKey("execucao_spsadt.codigo_execucao")
    )
    execucao_spsadt: Mapped["ExecucaoSPSADT"] = relationship(back_populates="transacao")
    data_registro_transacao = mapped_column(Date)
    hora_registro_transacao = mapped_column(Time)
    transacao_status: Mapped[List["TransacaoStatus"]] = relationship(
        back_populates="transacao"
    )
