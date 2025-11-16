from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,Integer,ForeignKey,Text


class ExecucaoSPSADT(db.Model):

    codigo_execucao : Mapped[int] = mapped_column(primary_key=True,unique=True)
    codigo_beneficiario : Mapped[int] = mapped_column(Integer,ForeignKey("numero_carteira"))
    codigo_contratado : Mapped[int] = mapped_column(Integer, ForeignKey("codigo_prestador_na_operadora"))
    codigo_solicitante : Mapped[int] = mapped_column(Integer, ForeignKey("codigo_solicitante"))
    login = Mapped[int] = mapped_column(Integer,ForeignKey("login"))
    indicacao_clinica : Mapped[bool]
    indicacao_acidente : Mapped[int] = mapped_column(comment="Ver tiss/schema.")
    observacao : Mapped[Text] = mapped_column(Text(length=500))
    senha : Mapped[str] = mapped_column(String(20))
    tipo_transacao : Mapped[str] = mapped_column(String(30))
