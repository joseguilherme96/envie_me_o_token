from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from sqlalchemy.orm import selectinload, joinedload
from src.models.db import db


class ExecucaoSPSADTRepository:
    def get_full_by_codigo_execucao(self, codigo_execucao: int):

        execucao_sp_sadt = (
            db.session.query(ExecucaoSPSADT)
            .options(
                selectinload(ExecucaoSPSADT.execucao_spsadt_procedimento),
                joinedload(ExecucaoSPSADT.beneficiario),
                joinedload(ExecucaoSPSADT.contratado),
                joinedload(ExecucaoSPSADT.solicitante),
                joinedload(ExecucaoSPSADT.operadora),
            )
            .filter(ExecucaoSPSADT.codigo_execucao == codigo_execucao)
            .first()
        )

        return {
            "codigo_execucao": execucao_sp_sadt.codigo_execucao,
            "codigo_beneficiario": execucao_sp_sadt.codigo_beneficiario,
            "codigo_contratado": execucao_sp_sadt.codigo_contratado,
            "codigo_solicitante": execucao_sp_sadt.codigo_solicitante,
            "operadora_registro_ans": execucao_sp_sadt.operadora_registro_ans,
            "indicacao_clinica": execucao_sp_sadt.indicacao_clinica,
            "observacao": execucao_sp_sadt.observacao,
            "tipo_transacao": execucao_sp_sadt.tipo_transacao,
            "login": execucao_sp_sadt.login,
            "indicacao_acidente": execucao_sp_sadt.indicacao_acidente,
            "senha": execucao_sp_sadt.senha,
            "beneficiario": {
                "numero_carteira": execucao_sp_sadt.beneficiario.numero_carteira,
                "atendimento_rn": execucao_sp_sadt.beneficiario.atendimento_rn,
                "nome_beneficiario": execucao_sp_sadt.beneficiario.nome_beneficiario,
            },
            "contratado": {
                "codigo_prestador_na_operadora": execucao_sp_sadt.contratado.codigo_prestador_na_operadora,
                "nome_contratado": execucao_sp_sadt.contratado.nome_contratado,
                "carater_atendimento": execucao_sp_sadt.contratado.carater_atendimento,
                "tipo_atendimento": execucao_sp_sadt.contratado.tipo_atendimento,
            },
            "solicitante": {
                "codigo_solicitante": execucao_sp_sadt.solicitante.codigo_solicitante,
                "profissional_solicitante": execucao_sp_sadt.solicitante.profissional_solicitante,
                "conselho_profissional": execucao_sp_sadt.solicitante.conselho_profissional,
                "numero_conselho_profissional": execucao_sp_sadt.solicitante.numero_conselho_profissional,
                "uf": execucao_sp_sadt.solicitante.uf,
                "cbos": execucao_sp_sadt.solicitante.cbos,
            },
            "operadora": {
                "registro_ans": execucao_sp_sadt.operadora.registro_ans,
                "operadora": execucao_sp_sadt.operadora.operadora,
            },
            "execucao_spsadt_procedimento": [
                {
                    "codigo_procedimento": proc.codigo_procedimento,
                    "codigo_execucao": proc.codigo_execucao,
                    "descricao_procedimento": proc.descricao_procedimento,
                    "quantidade_solicitada": proc.quantidade_solicitada,
                }
                for proc in execucao_sp_sadt.execucao_spsadt_procedimento
            ],
        }
