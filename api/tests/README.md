# Conftest.py

No arquivo conftest.py, possui alguma fixtures e ganchos de inicialização

## Gancho pytest_addoption

Adiciona algumas flags customizadas que permitem a mudança do banco de dados que esta sendo testado ou ainda, permite definir uma opção para testar em um ambiente diferente. 

## Flags 

### `--dburl`

Por está flag permite a mudança de um banco de dados SQLite que esta sendo usado para os testes para um banco de dados real MySQL por exemplo. Começar os testes com SQLite faz com que os testes se tornem mais rápidos, devido ser um banco em memoria, mas não garante que os testes serão executados com sucesso em um banco real, por isso o motivo da existência da flag, onde possibilita a mudança de banco apara que o testes ser executados em banco diferentes. 

### `--enviroment`

Está flag permite mudar o pytest rapidamente para que seja possivel testar a aplicação em ambientes diferentes, seja development, testing ou staging.

## Gancho `pytest_sessionstart`

Este gancho executa umas validações antes do teste prosseguir, garantindo que os teste não quebrem no meio do caminho por falta de alguma configuração. O ganho valida se conexão do banco de dados é feita com sucesso, se a conexão com o servidor flask é feita com sucesso ou ainda se o ambiente de teste é o mesmo ambiente que o flask está sendo executado fazendo com que os testes rodem somente quando estás configurações estão ok.

# Fixtures `set_test_settigs`
Está fixture seta o ambiente na variavel `ENV_FOR_DYNACONF` que foi definido na flag `--enviroment`, caso não seja definido, vem como default o ambiente `testing`.

A fixture também verifica se a váriavel `DYNACONF_USE_CLASS_FAKE` está setada, esta váriavel define que os testes usarão classes Fakes caso esteja setada com True.

## Por que testar `classes Fakes` ?

Estas classes foram usadas no inicio do projeto para testar validar o comportamento do codigo junto com classes abstratas sem criar o codido da implementação real validando a ideia da aplicação, após finalizado a imprementação concretada, não será mais válido testar apenas os comportamento, mas sim , deixar a váriável `DYNACONF_USE_CLASS_FAKE` defina como `false` para testar sempre a implementação real da aplicação.

# Fixture `app`

É responsável por criar o setup inicial da aplicação para execução dos testes, cria o app, coloca aplicação dentro de um gerenciador de contexto, e cria o banco de dados para execução dos testes.

Um retorno do app é feito para o teste os testes que o chama esta fixture.

Apóes a execução de todos os testes, o teardown é feito, destruindo todo o banco, sessoes e liberado o banco de dados utlizado.