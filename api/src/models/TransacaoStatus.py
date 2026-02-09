from __future__ import annotations
from .db import db
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TransacaoStatus(db.Model):
    codigo_transacao_status: Mapped[int] = mapped_column(primary_key=True, unique=True)
    codigo_transacao: Mapped[int] = mapped_column(
        ForeignKey("transacao.sequencia_transacao")
    )
    transacao: Mapped[Transacao] = relationship(back_populates="transacao_status")
    codigo_status: Mapped[int] = mapped_column(comment="Ver tiss/schema.")
    data_hora = mapped_column(DateTime)
