# Envie Me O Token -  Em desenvolvimento....

Será criada uma interface para que o paciente possa enviar o token gerado em seu dispositivo, ao enviar , será acionando um RPA que enviará uma solicitação a um web service SOAP afim de autorizar a sessão para o paciente realizar o tratamento sem a necessidade da recepicionista inserir o token de forma manual ganhando agilidade no atendimento do paciente.

# Objetivo deste projeto

Além de resolver um problema real, tem finalidade também de aplicar os conhecimentos já adiquiridos, como também ganhar novas experiências com os conhecimentos adiquiridos.

## O que este projeto espera alcançar.
- Uma análise profundas de documentações técnicas, desenvover com planejamento co  abertura de issues, desenvolver e entregar uma solução real.
- Entregar Fluxogramas de 2 RPAs(Geração de link automatico para usuário enviar o token e processo automatico de autorização do paciente para tratamento) que serão executados estabelecendo uma visão ampla de todo seu funcionamento.
- Compreensão de integração com web service SOAP
- Compreensão e Manipulação de arquivos/schemas XML.
- Compressão de leituras de documentação técnicas.
- Seguir padrões de comunicação estabelecidos pela ANS seguindo o padrão `TISS - Troca de Informação na Saúde Suplementar`
- Desenvolver o RPA orientado as testes `TDD - Test Driven Develoment` com `Pytest`
- - Testes conceituais
- - Testes de Zombaria(Mocks)
- - Criar testes unitários
- - Criar testes de integração
- - Desenvolver a API que receberá o token enviado do usuário e os códigos de processamento dos RPAs.
- Trabalhar com `ORM - Object Relational Mapping` com `Flask-Alchemy`
- Geração de visualização gráfica do `DER - Diagrama Entidade-Relacionamento` com `Graphviz`
- Usufruir de Migrações com `Flask-Migration`
- Trabalhar com ambientes de `Teste`, `Homologação` e `Produção`.
- Desenvolver uma tela simples com `Webpack + Vue.js + Vuetify` que acionará o RPA.

# Fluxograma do RPA

Serão desenvolvidos 2 RPAs :

- O primeiro RPA com detalhe `A` do lado esquerdo vai gerar o link de acesso para o paciente poder acessar a tela que ele vai inserir o token e enviar. - Já o segundo RPA com detalhe `B` do lado direito vai ser acionado a partir do momento que o paciente inserir o token e enviar.

[![Fluxograma RPA](assets/fluxograma_RPA.png "Fluxograma RPA")](assets/fluxograma_RPA.png)

# Schema do Banco de Dados

Uma imagem do schema do banco de dados é gerado automaticamente após apartir das models que foram criadas na pasta `api/src/models`.

Para gerar a imagem do schema do banco de dados automaticamente execute um dos seguintes comandos abaixo :

``` sh
    
    # Na raiz do projeto
    set pythonpath=api/src && python api/src/schema/generate_schema.py

    # Ou dentro da pasta interface
    cd interface
    npm run schema:bd

```

## Imagem do Schema

[![Imagem do schema do banco de dados](api/src/schema/db.svg "Imagem do schema do banco de dados")](api/src/schema/db.svg)

# Execução do projeto via docker

Execute o seguinte comando :

```sh
    npm start
```

- O docker irá subir o banco de dados MySQL.
- Instalar as dependências do projeto.
- Subir o servidor Flask para desenvolvimento.


