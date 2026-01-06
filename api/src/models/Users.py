from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy import Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import logging

class Users(db.Model):

    login : Mapped[str] = mapped_column(String(length=30),unique=True,primary_key=True)
    senha : Mapped[str] = mapped_column(String(255))
    tipo_usuario_id : Mapped[int] = mapped_column(ForeignKey("tipo_user.cod_tipo_user"))
    users : Mapped[TipoUser] = relationship(back_populates="users")
    execucao_spsadt : Mapped[List["ExecucaoSPSADT"]] = relationship(back_populates="users")

    def inserir(user):
        try:
            db.session.begin()
            db.session.add(user)
            db.session.commit()
            return {
                "login": user.login,
                "tipo_usuario_id": user.tipo_usuario_id
            }
        except Exception as e:
            db.session.rollback()
            raise

    def buscar(where):

        try:

            query = db.select(Users)

            if where.get("login"):

                query = query.where(Users.login == where['login'])

            logging.debug(query)
            execute = db.session.execute(query)

            return execute.fetchall()
        
        except Exception as e:

            raise
    
        finally:
            db.session.close()