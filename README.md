<h1 align="center">
📄<br>README - Projeto Sistema UBER
</h1>

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Pré requisitos](#pré-requisitos)
* [Execução](#execução)
* [Implantação](#implantação)
* [Bibliotecas](#bibliotecas)

# Descrição do projeto
> Este repositório é meu projeto Python de criação de um sistema, criado a partir de janela Tkinter, que permite a integração diária de valores referente aos ganhos de um motorista de aplicativo (Uber/99) em uma planilha de controle mensal.

# Funcionalidades e Demonstração da Aplicação
Atualização de uma planilha de controle mensal dos ganhos e gastos de um motorista de aplicativo:
- número de dias em que o motorista utilizou o sistema (teoricamente, seria o número de dias trabalhados no mês;
- valores ganhos nos diferentes aplicativos utilizados;
- valores gastos/despesas;
- valor médio por dia trabalhado;
- valor líquido do mês.

Interface do sistema de inserção de dados:<br>
![Screenshot_1](https://user-images.githubusercontent.com/128300382/227021545-589f3042-3afa-41f9-8cc5-bc6e8ddbb975.png)

Feedback instantâneo do sistema após preenchimento:<br>
![Screenshot_2](https://user-images.githubusercontent.com/128300382/227021551-aac20e89-421c-4a97-bed6-1b7a5f0d8223.png)

Planilha de controle atualizada:<br>
![Screenshot_3](https://user-images.githubusercontent.com/128300382/227021555-98486089-3d86-4104-b70b-feb68054ca4a.png)

## Pré requisitos

* Sistema operacional Windows
* IDE de python (ambiente de desenvolvimento integrado de python)
* Planilha de controle (arquivo excel)

## Execução

Na execução deste projeto, ao preencher os campos de input do sistema, automaticamente a planilha de controle será atualizada. O sistema foi criado para uso diário, somando-se 1 dia a mais na planilha, representando dessa forma 1 dia trabalhado pelo motorista de aplicativo.

## Implantação

É possível adaptar este projeto a qualquer outro modelo de inserção de dados. A partir destes dados, a planilha será automaticamente atualizada para controle mês a mês.

## Bibliotecas

* pandas: biblioteca de análise de dados
* datetime: biblioteca usada para definir data e horário
* os: biblioteca de integração de arquivos e pastas do computador
* tkinter: biblioteca de criação de janelas/sistemas
