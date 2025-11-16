from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,Integer,ForeignKey


class ExecucaoSPSADTProcedimento(db.Model):

    codigo_execucao : Mapped[int] = mapped_column(Integer,ForeignKey("codigo_execucao"))
    codigo_procedimento : Mapped[int] = mapped_column(comment="Ver na guia do paciente.")
    descricao_procedimento : Mapped[str] = mapped_column(String(150),comment="Ver na guia do paciente.")
    quantidade_solicitada : Mapped[int]