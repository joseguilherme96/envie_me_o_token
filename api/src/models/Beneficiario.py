from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
import logging


class Beneficiario(db.Model):
    numero_carteira: Mapped[str] = mapped_column(String(20), primary_key=True)
    execucao_spsadt: Mapped[List[ExecucaoSPSADT]] = relationship(
        back_populates="beneficiario"
    )
    atendimento_rn: Mapped[bool] = mapped_column(
        Boolean, comment="Define se beneficiário é rem nascido."
    )
    nome_beneficiario: Mapped[str] = mapped_column(String(70), nullable=False)

    def inserir(beneficiario):
        try:
            db.session.begin()
            db.session.add(beneficiario)
            db.session.commit()
            return {
                "numero_carteira": beneficiario.numero_carteira,
                "nome_beneficiario": beneficiario.nome_beneficiario,
                "atendimento_rn": beneficiario.atendimento_rn,
            }
        except Exception as e:
            db.session.rollback()
            raise

        finally:
            db.session.close()

    def buscar(where):

        try:
            logging.debug(where)

            query = db.select(Beneficiario)

            logging.debug(query)

            if where.get("numero_carteira"):
                query = query.where(
                    Beneficiario.numero_carteira == where["numero_carteira"]
                )

            if where.get("atendimento_rn"):
                query = query.where(
                    Beneficiario.atendimento_rn == where["atendimento_rn"]
                )

            if where.get("nome_beneficiario"):
                query = query.where(
                    Beneficiario.nome_beneficiario == where["nome_beneficiario"]
                )

            logging.debug(query)

            execute = db.session.execute(query)

            logging.debug(execute)

            return execute.fetchall()

        except Exception as e:
            raise

        finally:
            db.session.close()
