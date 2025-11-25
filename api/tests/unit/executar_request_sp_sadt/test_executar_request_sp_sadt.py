from src.factory.factory_request_spsadt import FactoryRequestSPSADT
from unittest.mock import patch
import os
from dotenv import load_dotenv

@patch("src.fake.fake_resquest_execucao_sp_sadat.requests.post")
def test_a_execucao_da_requisicao_sp_sadt_deve_ser_feita_com_sucesso(mock_request_post):

    ler_todo_conteudo_solicitacao_xml = """
    
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

    ler_todo_conteudo_solicitacao_xml = ler_todo_conteudo_solicitacao_xml.format(
        tipo_transacao="",
        sequencial_transacao="",
        data_registro_transacao="",
        hora_registro_transacao="",
        codigo_prestador_na_operadora="",
        registro_ANS="",
        numero_guia_operadora="",
        padrao="",
        login_prestador="",
        senha_prestador="",
        numero_guia_prestador="",
        tipo_etapa_autorizacao="",
        numero_carteira="",
        atendimento_rn="",
        nome_beneficiario="",
        identificador_beneficiario="",
        codigo_prestado_na_operadora="",
        nome_contratado="",
        nome_profissional="",
        conselho_profissional="",
        numero_conselho_profissional="",
        uf="",
        cbos="",
        carater_atendimento="",
        data_solicitacao="",
        indicacao_clinica="",
        tipo_atendimento="",
        indicacao_acidente="",
        codigo_procedimento="",
        descricao_procedimento="",
        quantidade_solicitada="",
        codigo_operadora="",
        observacao="",
        hash=""
    )

    ler_todo_conteudo_xml = """

    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:ans="http://www.ans.gov.br/padroes/tiss/schemas"
        xmlns:xd="http://www.w3.org/2000/09/xmldsig#">
        <soapenv:Header />
        <soapenv:Body>
            <ans:autorizacaoProcedimentoWS>
                <ans:cabecalho>
                    <ans:identificacaoTransacao>
                        <ans:tipoTransacao>RESPOSTA_SOLICITACAO</ans:tipoTransacao>
                        <ans:sequencialTransacao>1111</ans:sequencialTransacao>
                        <ans:dataRegistroTransacao>2016-12-01</ans:dataRegistroTransacao>
                        <ans:horaRegistroTransacao>12:00:00</ans:horaRegistroTransacao>
                    </ans:identificacaoTransacao>
                    <ans:origem>
                        <ans:registroANS>111111</ans:registroANS>
                    </ans:origem>
                    <ans:destino>
                        <ans:identificacaoPrestador>
                            <ans:CNPJ>00111222000100</ans:CNPJ>
                        </ans:identificacaoPrestador>
                    </ans:destino>
                    <ans:Padrao>3.03.01</ans:Padrao>
                    <ans:loginSenhaPrestador>
                        <ans:loginPrestador>TESTE001</ans:loginPrestador>
                        <ans:senhaPrestador>9c4c9c4c9c4c9c4c9c4c9c4c9c4c9c4c</ans:senhaPrestador>
                    </ans:loginSenhaPrestador>
                </ans:cabecalho>
                <ans:autorizacaoProcedimento>
                    <ans:autorizacaoServico>
                        <ans:dadosAutorizacao>
                            <ans:numeroGuiaPrestador>1111</ans:numeroGuiaPrestador>
                            <ans:numeroGuiaOperadora>2222</ans:numeroGuiaOperadora>
                            <ans:dataAutorizacao>2016-12-01</ans:dataAutorizacao>
                            <ans:senha>000000001</ans:senha>
                        </ans:dadosAutorizacao>
                        <ans:dadosBeneficiario>
                            <ans:numeroCarteira>1111111111111</ans:numeroCarteira>
                            <ans:atendimentoRN>N</ans:atendimentoRN>
                            <ans:nomeBeneficiario>BENEFICIARIO</ans:nomeBeneficiario>
                        </ans:dadosBeneficiario>
                        <ans:prestadorAutorizado>
                            <ans:dadosContratado>
                                <ans:codigoPrestadorNaOperadora>1111</ans:codigoPrestadorNaOperadora>
                                <ans:nomeContratado>CONTRATADO</ans:nomeContratado>
                            </ans:dadosContratado>
                            <ans:cnesContratado>9999999</ans:cnesContratado>
                        </ans:prestadorAutorizado>
                        <ans:statusSolicitacao>1</ans:statusSolicitacao>
                        <ans:servicosAutorizados>
                            <ans:servicoAutorizado>
                                <ans:procedimento>
                                    <ans:codigoTabela>22</ans:codigoTabela>
                                    <ans:codigoProcedimento>40101010</ans:codigoProcedimento>
                                    <ans:descricaoProcedimento>ECG CONVENCIONAL DE AT</ans:descricaoProcedimento>
                                </ans:procedimento>
                                <ans:quantidadeSolicitada>1</ans:quantidadeSolicitada>
                                <ans:quantidadeAutorizada>1</ans:quantidadeAutorizada>
                            </ans:servicoAutorizado>
                        </ans:servicosAutorizados>
                    </ans:autorizacaoServico>
                </ans:autorizacaoProcedimento>
                <ans:hash>A551AF234DF921F8AA6CEAC4E2FE579D</ans:hash>
            </ans:autorizacaoProcedimentoWS>
        </soapenv:Body>
    </soapenv:Envelope>

    """
    mock_request_post.return_value.text = ler_todo_conteudo_xml

    load_dotenv("api/.env")
    uri =  os.getenv("API_SOAP_AUTORIZACAO_EXECUCAO_SP_SADT")

    request_sp_sadt = FactoryRequestSPSADT.create(uri)

    status_code, text = request_sp_sadt.executar_request_sp_sadt(ler_todo_conteudo_solicitacao_xml)
    assert text == ler_todo_conteudo_xml