from __future__ import annotations
from typing import List
from .db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
import logging

class Solicitante(db.Model):

    codigo_solicitante : Mapped[int] = mapped_column(primary_key=True,unique=True)
    profissional_solicitante : Mapped[str] = mapped_column(String(70))
    conselho_profissional : Mapped[int]
    numero_conselho_profissional : Mapped[str] = mapped_column(String(15))
    uf : Mapped[int]
    cbos : Mapped[int]
    execucao_spsadt : Mapped[List["ExecucaoSPSADT"]] = relationship(back_populates="solicitante")

    def buscar(where):
        try:
            logging.debug(where)
            query = db.select(Solicitante)
            
            if where.get("codigo_solicitante"):
                query = query.where(Solicitante.codigo_solicitante == where["codigo_solicitante"])
            
            if where.get("profissional_solicitante"):
                query = query.where(Solicitante.profissional_solicitante == where["profissional_solicitante"])
            
            if where.get("conselho_profissional"):
                query = query.where(Solicitante.conselho_profissional == where["conselho_profissional"])
            
            if where.get("numero_conselho_profissional"):
                query = query.where(Solicitante.numero_conselho_profissional == where["numero_conselho_profissional"])
            
            if where.get("uf"):
                query = query.where(Solicitante.uf == where["uf"])
            
            if where.get("cbos"):
                query = query.where(Solicitante.cbos == where["cbos"])
            
            logging.debug(query)
            execute = db.session.execute(query)
            return execute.fetchall()
        
        except Exception as e:
            raise
        
        finally:
            db.session.close()

    def inserir(solicitante):
        try:
            db.session.begin()
            db.session.add(solicitante)
            db.session.commit()
            return {
                "codigo_solicitante": solicitante.codigo_solicitante,
                "profissional_solicitante": solicitante.profissional_solicitante,
                "conselho_profissional": solicitante.conselho_profissional,
                "numero_conselho_profissional": solicitante.numero_conselho_profissional,
                "uf": solicitante.uf,
                "cbos": solicitante.cbos
            }
        except Exception as e:
            db.session.rollback()
            raise