# GranaCheck - Agente Financeiro Inteligente

## Descrição

O GranaCheck é um agente simples criado para ajudar pessoas a controlarem seus gastos mensais.

O foco do agente é identificar quando o usuário está próximo do limite de gastos ou quando já ultrapassou o valor definido.

## Problema Resolvido

Muitas pessoas têm dificuldade em acompanhar seus gastos durante o mês.  
Isso pode causar descontrole financeiro, compras desnecessárias e falta de planejamento.

O GranaCheck resolve esse problema oferecendo alertas simples e diretos.

## Personalidade do Agente

O agente possui uma comunicação:

- Informal
- Direta
- Simples
- Sem termos técnicos
- Focada em ajudar o usuário a tomar decisões rápidas

Exemplo de resposta:

> Você passou do limite! Bora segurar os gastos esse mês.

## O que o agente pode fazer

- Receber o limite mensal informado pelo usuário
- Receber o gasto atual
- Comparar os valores
- Gerar alertas financeiros
- Exibir um resumo simples dos dados

## O que o agente não faz

- Não acessa conta bancária real
- Não realiza investimentos
- Não substitui um consultor financeiro
- Não toma decisões pelo usuário
- Não fornece aconselhamento financeiro profissional

## Arquitetura Simples

```text
Usuário informa limite e gasto
        ↓
Sistema processa os dados
        ↓
Agente compara gasto com limite
        ↓
Agente retorna alerta ou confirmação
