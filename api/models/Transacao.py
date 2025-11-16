from db import db
from sqlalchemy import Integer, String, ForeignKey,Date,Time
from sqlalchemy.orm import Mapped, mapped_column


class Transacao(db.Model):

    sequencia_transacao : Mapped[int] = mapped_column(primary_key=True,autoincrement=True,unique=True)
    codigo_execucao_sp_sadt : Mapped[int] = mapped_column(Integer, ForeignKey("codigo_execucao"))
    data_registro_transacao = mapped_column(Date)
    hora_registro_transacao = mapped_column(Time)