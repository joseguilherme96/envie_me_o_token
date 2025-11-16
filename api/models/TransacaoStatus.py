from db import db
from sqlalchemy import Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import Mapped, mapped_column

class TransacaoStatus(db.Model):

    codigo_transacao_status : Mapped[int] = mapped_column(primary_key=True, unique=True)
    codigo_transacao : Mapped[int] = mapped_column(ForeignKey("sequencia_transacao"))
    codigo_status : Mapped[int] = mapped_column(comment="Ver tiss/schema.")
    data_hora = mapped_column(DateTime)