from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Text
import logging


class ExecucaoSPSADT(db.Model):
    codigo_execucao: Mapped[int] = mapped_column(
        primary_key=True, unique=True, autoincrement=True
    )
    codigo_beneficiario: Mapped[str] = mapped_column(
        ForeignKey("beneficiario.numero_carteira")
    )
    beneficiario: Mapped["Beneficiario"] = relationship(
        back_populates="execucao_spsadt"
    )
    codigo_contratado: Mapped[int] = mapped_column(
        ForeignKey("contratado.codigo_prestador_na_operadora")
    )
    contratado: Mapped["Contratado"] = relationship(back_populates="execucao_spsadt")
    codigo_solicitante: Mapped[int] = mapped_column(
        ForeignKey("solicitante.codigo_solicitante")
    )
    solicitante: Mapped["Solicitante"] = relationship(back_populates="execucao_spsadt")
    operadora_registro_ans: Mapped[int] = mapped_column(
        ForeignKey("operadora.registro_ans")
    )
    operadora: Mapped["Operadora"] = relationship(back_populates="execucao_spsadt")
    login: Mapped[str] = mapped_column(String(length=30), ForeignKey("users.login"))
    users: Mapped["Users"] = relationship(back_populates="execucao_spsadt")
    indicacao_clinica: Mapped[bool] = mapped_column(
        comment="A indicação clinica é descrita pelo médico"
    )
    indicacao_acidente: Mapped[int] = mapped_column(comment="Ver tiss/schema.")
    observacao: Mapped[Text] = mapped_column(Text(length=500))
    senha: Mapped[str] = mapped_column(String(20))
    tipo_transacao: Mapped[str] = mapped_column(String(30))
    transacao: Mapped[list["Transacao"]] = relationship(
        back_populates="execucao_spsadt"
    )
    execucao_spsadt_procedimento: Mapped[List["ExecucaoSPSADTProcedimento"]] = (
        relationship(back_populates="execucao_spsadt")
    )

    def buscar(where):
        try:
            logging.debug(where)
            query = db.select(ExecucaoSPSADT)

            if where.get("codigo_execucao"):
                query = query.where(
                    ExecucaoSPSADT.codigo_execucao == where["codigo_execucao"]
                )

            if where.get("codigo_beneficiario"):
                query = query.where(
                    ExecucaoSPSADT.codigo_beneficiario == where["codigo_beneficiario"]
                )

            if where.get("codigo_contratado"):
                query = query.where(
                    ExecucaoSPSADT.codigo_contratado == where["codigo_contratado"]
                )

            if where.get("codigo_solicitante"):
                query = query.where(
                    ExecucaoSPSADT.codigo_solicitante == where["codigo_solicitante"]
                )

            if where.get("operadora_registro_ans"):
                query = query.where(
                    ExecucaoSPSADT.operadora_registro_ans
                    == where["operadora_registro_ans"]
                )

            if where.get("login"):
                query = query.where(ExecucaoSPSADT.login == where["login"])

            logging.debug(query)
            execute = db.session.execute(query)
            return execute.fetchall()

        except Exception as e:
            raise

        finally:
            db.session.close()

    def inserir(execucao):
        try:
            db.session.begin()
            db.session.add(execucao)
            db.session.commit()
            return {
                "codigo_execucao": execucao.codigo_execucao,
                "codigo_beneficiario": execucao.codigo_beneficiario,
                "codigo_contratado": execucao.codigo_contratado,
                "codigo_solicitante": execucao.codigo_solicitante,
                "operadora_registro_ans": execucao.operadora_registro_ans,
                "login": execucao.login,
                "indicacao_clinica": execucao.indicacao_clinica,
                "indicacao_acidente": execucao.indicacao_acidente,
                "observacao": execucao.observacao,
                "senha": execucao.senha,
                "tipo_transacao": execucao.tipo_transacao,
            }
        except Exception as e:
            db.session.rollback()
            raise

    def select(where={}):

        return []
