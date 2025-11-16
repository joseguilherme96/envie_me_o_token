from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,Boolean

class Beneficiario(db.Model):

    numero_carteira : Mapped[str] = mapped_column(String(20),nullable=False)
    atendimento_rn : Mapped[bool] = mapped_column(Boolean,comment="Define se beneficiário é rem nascido.")
    nome_beneficiario : Mapped[str] = mapped_column(String(70),nullable=False)