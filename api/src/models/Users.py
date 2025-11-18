from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy import Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(db.Model):

    login : Mapped[str] = mapped_column(unique=True,primary_key=True)
    senha : Mapped[str] = mapped_column(String(30))
    tipo_usuario_id : Mapped[int] = mapped_column(ForeignKey("tipo_user.cod_tipo_user"))
    users : Mapped[UserTipo] = relationship(back_populates="users")
    execucao_spsadt : Mapped[List["ExecucaoSPSADT"]] = relationship(back_populates="users")
    