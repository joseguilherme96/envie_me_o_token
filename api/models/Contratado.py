from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Contratado(db.Model):

    codigo_prestador_na_operadora : Mapped[int] = mapped_column(unique=True,primary_key=True,comment="O codigo do prestador é definido na operadora.")
    nome_contratado : Mapped[str] = mapped_column(String(70),nullable=False)
    carater_atendimento : Mapped[int] = mapped_column(comment="1 - Eletiva, 2 - Urgência/Emergencia")
    tipo_atendimento : Mapped[int] = mapped_column(comment="Ver tiss/schemas.")