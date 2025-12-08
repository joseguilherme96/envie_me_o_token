from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy import Integer, String, Enum, ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TipoUser(db.Model):
    
    cod_tipo_user : Mapped[int] = mapped_column(unique=True,primary_key=True)
    tipo : Mapped[str] = mapped_column(String(50), Enum('Prestador','Beneficiario', name='tipo_user_enum'))
    users : Mapped[List[Users]] = relationship(back_populates="users")

    def inserir(TipoUser):

        try:

            db.session.begin()

            db.session.add(TipoUser)
            db.session.commit()

            return {
                "cod_tipo_user":TipoUser.cod_tipo_user,
                "tipo":TipoUser.tipo
            }

        except Exception as e:

            db.session.rollback()

            raise