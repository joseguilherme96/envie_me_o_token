from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum
import logging

valores = [str(i) for i in range(1, 23)]


class Contratado(db.Model):
    codigo_prestador_na_operadora: Mapped[int] = mapped_column(
        unique=True,
        primary_key=True,
        comment="O codigo do prestador é definido na operadora.",
    )
    nome_contratado: Mapped[str] = mapped_column(String(70), nullable=False)
    carater_atendimento: Mapped[str] = mapped_column(
        Enum("1", "2"), comment="1 - Eletiva, 2 - Urgência/Emergencia"
    )
    tipo_atendimento: Mapped[str] = mapped_column(
        Enum(*valores, name="tipo_atendimento_enum", validate_strings=False),
        comment="Ver tiss/schemas.",
    )
    execucao_spsadt: Mapped[List["ExecucaoSPSADT"]] = relationship(
        back_populates="contratado"
    )

    def inserir(contratado):
        try:
            db.session.begin()
            db.session.add(contratado)
            db.session.commit()
            return {
                "codigo_prestador_na_operadora": contratado.codigo_prestador_na_operadora,
                "nome_contratado": contratado.nome_contratado,
                "carater_atendimento": str(contratado.carater_atendimento),
                "tipo_atendimento": contratado.tipo_atendimento,
            }
        except Exception as e:
            db.session.rollback()
            raise

    def buscar(where):

        try:
            logging.debug(where)

            query = db.select(Contratado)

            logging.debug(query)

            if where.get("codigo_prestador_na_operadora"):
                query = query.where(
                    Contratado.codigo_prestador_na_operadora
                    == where["codigo_prestador_na_operadora"]
                )

            if where.get("nome_contratado"):
                query = query.where(
                    Contratado.nome_contratado == where["nome_contratado"]
                )

            if where.get("carater_atendimento"):
                query = query.where(
                    Contratado.carater_atendimento == where["carater_atendimento"]
                )

            if where.get("tipo_atendimento"):
                query = query.where(
                    Contratado.tipo_atendimento == where["tipo_atendimento"]
                )

            logging.debug(query)

            execute = db.session.execute(query)

            logging.debug(execute)

            return execute.fetchall()

        except Exception as e:
            raise

        finally:
            db.session.close()
