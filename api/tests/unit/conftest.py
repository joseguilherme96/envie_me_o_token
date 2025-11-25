from pytest import fixture

@fixture
def template_data_xml_request():

    return """

        <soapenv:Envelope
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:sch="http://www.ans.gov.br/padroes/tiss/schemas"
            xmlns:xd="http://www.w3.org/2000/09/xmldsig#">
            <soapenv:Header />
            <soapenv:Body>
                <sch:solicitacaoProcedimentoWS>
                    <sch:cabecalho>
                        <sch:identificacaoTransacao>
                            <sch:tipoTransacao>{tipo_transacao}</sch:tipoTransacao>
                            <sch:sequencialTransacao>{sequencial_transacao}</sch:sequencialTransacao>
                            <sch:dataRegistroTransacao>{data_registro_transacao}</sch:dataRegistroTransacao>
                            <sch:horaRegistroTransacao>{hora_registro_transacao}</sch:horaRegistroTransacao>
                        </sch:identificacaoTransacao>
                        <sch:origem>
                            <sch:identificacaoPrestador>
                                <sch:codigoPrestadorNaOperadora>{codigo_prestador_na_operadora}</sch:codigoPrestadorNaOperadora>
                            </sch:identificacaoPrestador>
                        </sch:origem>
                        <sch:destino>
                            <sch:registroANS>{registro_ANS}</sch:registroANS>
                            <sch:numeroGuiaOperadora>{numero_guia_operadora}</sch:numeroGuiaOperadora>
                        </sch:destino>
                        <sch:padrao>{padrao}</sch:padrao>
                        <sch:loginSenhaPrestador>
                            <sch:loginPrestador>{login_prestador}</sch:loginPrestador>
                            <sch:senhaPrestador>{senha_prestador}</sch:senhaPrestador>
                        </sch:loginSenhaPrestador>
                    </sch:cabecalho>
                    <sch:solicitacaoProcedimento>
                        <sch:solicitacaoSP-SADT>
                            <sch:cabecalhoSolicitacao>
                                <sch:registroANS>{registro_ANS}</sch:registroANS>
                                <sch:numeroGuiaPrestador>{numero_guia_prestador}</sch:numeroGuiaPrestador>
                            </sch:cabecalhoSolicitacao>
                            <sch:tipoEtapaAutorizacao>{tipo_etapa_autorizacao}</sch:tipoEtapaAutorizacao>
                            <sch:dadosBeneficiario>
                                <sch:numeroCarteira>{numero_carteira}</sch:numeroCarteira>
                                <sch:atendimentoRN>{atendimento_rn}</sch:atendimentoRN>
                                <sch:nomeBeneficiario>{nome_beneficiario}</sch:nomeBeneficiario>
                                <sch:identificadorBeneficiario>{identificador_beneficiario}</sch:identificadorBeneficiario>
                            </sch:dadosBeneficiario>
                            <sch:dadosSolicitante>
                                <sch:contratadoSolicitante>
                                    <sch:codigoPrestadorNaOperadora>{codigo_prestado_na_operadora}</sch:codigoPrestadorNaOperadora>
                                    <sch:nomeContratado>{nome_contratado}</sch:nomeContratado>
                                </sch:contratadoSolicitante>
                                <sch:profissionalSolicitante>
                                    <sch:nomeProfissional>{nome_profissional}</sch:nomeProfissional>
                                    <sch:conselhoProfissional>{conselho_profissional}</sch:conselhoProfissional>
                                    <sch:numeroConselhoProfissional>{numero_conselho_profissional}</sch:numeroConselhoProfissional>
                                    <sch:UF>{uf}</sch:UF>
                                    <sch:CBOS>{cbos}</sch:CBOS>
                                </sch:profissionalSolicitante>
                            </sch:dadosSolicitante>
                            <sch:caraterAtendimento>{carater_atendimento}</sch:caraterAtendimento>
                            <sch:dataSolicitacao>{data_solicitacao}</sch:dataSolicitacao>
                            <sch:indicacaoClinica>{indicacao_clinica}</sch:indicacaoClinica>
                            <sch:tipoAtendimento>{tipo_atendimento}</sch:tipoAtendimento>
                            <sch:indicacaoAcidente>{indicacao_acidente}</sch:indicacaoAcidente>
                            <sch:procedimentosSolicitados>
                                <sch:procedimento>
                                    <sch:codigoProcedimento>{codigo_procedimento}</sch:codigoProcedimento>
                                    <sch:descricaoProcedimento>{descricao_procedimento}</sch:descricaoProcedimento>
                                </sch:procedimento>
                                <sch:quantidadeSolicitada>{quantidade_solicitada}</sch:quantidadeSolicitada>
                            </sch:procedimentosSolicitados>
                            <sch:dadosExecutante>
                                <sch:codigoOperadora>{codigo_operadora}</sch:codigoOperadora>
                                <sch:nomeContratado>{nome_contratado}</sch:nomeContratado>
                            </sch:dadosExecutante>
                            <sch:observacao>{observacao}</sch:observacao>
                        </sch:solicitacaoSP-SADT>
                    </sch:solicitacaoProcedimento>
                    <sch:hash>{hash}</sch:hash>
                </sch:solicitacaoProcedimentoWS>
            </soapenv:Body>
        </soapenv:Envelope>

    """

import pytest

@pytest.fixture
def template_data_xml_response():
    template = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:ans="http://www.ans.gov.br/padroes/tiss/schemas"
        xmlns:xd="http://www.w3.org/2000/09/xmldsig#">
        <soapenv:Header />
        <soapenv:Body>
            <ans:autorizacaoProcedimentoWS>
                <ans:cabecalho>
                    <ans:identificacaoTransacao>
                        <ans:tipoTransacao>{tipo_transacao}</ans:tipoTransacao>
                        <ans:sequencialTransacao>{sequencial_transacao}</ans:sequencialTransacao>
                        <ans:dataRegistroTransacao>{data_registro}</ans:dataRegistroTransacao>
                        <ans:horaRegistroTransacao>{hora_registro}</ans:horaRegistroTransacao>
                    </ans:identificacaoTransacao>
                    <ans:origem>
                        <ans:registroANS>{registro_ans}</ans:registroANS>
                    </ans:origem>
                    <ans:destino>
                        <ans:identificacaoPrestador>
                            <ans:CNPJ>{cnpj}</ans:CNPJ>
                        </ans:identificacaoPrestador>
                    </ans:destino>

                    <ans:Padrao>{padrao}</ans:Padrao>

                    <ans:loginSenhaPrestador>
                        <ans:loginPrestador>{login}</ans:loginPrestador>
                        <ans:senhaPrestador>{senha}</ans:senhaPrestador>
                    </ans:loginSenhaPrestador>
                </ans:cabecalho>

                <ans:autorizacaoProcedimento>
                    <ans:autorizacaoServico>
                        <ans:dadosAutorizacao>
                            <ans:numeroGuiaPrestador>{guia_prestador}</ans:numeroGuiaPrestador>
                            <ans:numeroGuiaOperadora>{guia_operadora}</ans:numeroGuiaOperadora>
                            <ans:dataAutorizacao>{data_autorizacao}</ans:dataAutorizacao>
                            <ans:senha>{senha_autorizacao}</ans:senha>
                        </ans:dadosAutorizacao>

                        <ans:dadosBeneficiario>
                            <ans:numeroCarteira>{numero_carteira}</ans:numeroCarteira>
                            <ans:atendimentoRN>{atendimento_rn}</ans:atendimentoRN>
                            <ans:nomeBeneficiario>{nome_beneficiario}</ans:nomeBeneficiario>
                        </ans:dadosBeneficiario>

                        <ans:prestadorAutorizado>
                            <ans:dadosContratado>
                                <ans:codigoPrestadorNaOperadora>{codigo_prestador}</ans:codigoPrestadorNaOperadora>
                                <ans:nomeContratado>{nome_contratado}</ans:nomeContratado>
                            </ans:dadosContratado>
                            <ans:cnesContratado>{cnes}</ans:cnesContratado>
                        </ans:prestadorAutorizado>

                        <ans:statusSolicitacao>{status_solicitacao}</ans:statusSolicitacao>

                        <ans:servicosAutorizados>
                            <ans:servicoAutorizado>
                                <ans:procedimento>
                                    <ans:codigoTabela>{codigo_tabela}</ans:codigoTabela>
                                    <ans:codigoProcedimento>{codigo_procedimento}</ans:codigoProcedimento>
                                    <ans:descricaoProcedimento>{descricao_procedimento}</ans:descricaoProcedimento>
                                </ans:procedimento>
                                <ans:quantidadeSolicitada>{quantidade_solicitada}</ans:quantidadeSolicitada>
                                <ans:quantidadeAutorizada>{quantidade_autorizada}</ans:quantidadeAutorizada>
                            </ans:servicoAutorizado>
                        </ans:servicosAutorizados>

                    </ans:autorizacaoServico>
                </ans:autorizacaoProcedimento>

                <ans:hash>{hash}</ans:hash>

            </ans:autorizacaoProcedimentoWS>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    return template
