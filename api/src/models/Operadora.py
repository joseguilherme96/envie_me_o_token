from __future__ import annotations
from typing import TYPE_CHECKING
from .db import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .ExecucaoSPSADT import ExecucaoSPSADT


class Operadora(db.Model):
    registro_ans: Mapped[int] = mapped_column(
        unique=True, primary_key=True, comment="Nº de registro da operadora na ANS."
    )
    operadora: Mapped[str] = mapped_column(String(30), comment="Nome da operadora")
    execucao_spsadt: Mapped[list[ExecucaoSPSADT]] = relationship(
        back_populates="operadora"
    )

    def buscar(where):

        try:
            query = db.select(Operadora)

            if where.get("registro_ans"):
                query = query.where(Operadora.registro_ans == where["registro_ans"])

            if where.get("operadora"):
                query = query.where(Operadora.operadora == int(where["operadora"]))

            execute = db.session.execute(query)

            return execute.fetchall()

        except Exception:
            raise

        finally:
            db.session.close()

    def inserir(operadora):
        try:
            db.session.begin()
            db.session.add(operadora)
            db.session.commit()
            return {
                "registro_ans": operadora.registro_ans,
                "operadora": operadora.operadora,
            }
        except Exception:
            db.session.rollback()
            raise
