from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy import Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TipoUser(db.Model):

    cod_tipo_user : Mapped[int] = mapped_column(unique=True,primary_key=True)
    tipo : Mapped[str] = mapped_column(String,Enum("Prestador","Beneficiario"))
    users : Mapped[List[Users]] = relationship(back_populates="users")