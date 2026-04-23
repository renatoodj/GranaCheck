# 💰 GranaCheck - Agente Financeiro Inteligente

---

## 📌 Descrição do Projeto

O GranaCheck é um agente inteligente simples desenvolvido para ajudar usuários a controlar seus gastos mensais de forma prática, rápida e objetiva.

O agente analisa os valores informados pelo usuário e gera alertas financeiros, auxiliando na tomada de decisões e evitando o descontrole financeiro.

---

## 🎯 Problema Resolvido

Muitas pessoas não conseguem acompanhar seus gastos durante o mês, o que pode levar a:

- Excesso de despesas
- Falta de planejamento financeiro
- Uso descontrolado do orçamento

O GranaCheck resolve esse problema oferecendo um monitoramento simples baseado em regras.

---

## 🧠 Etapa 1 - Documentação do Agente

### 🏷️ Nome do Agente
**GranaCheck**

### 🎯 Objetivo
Auxiliar o usuário a controlar seus gastos mensais e evitar ultrapassar o limite financeiro definido.

---

## 🎭 Personalidade do Agente

O agente possui um comportamento:

- Informal
- Direto
- Objetivo
- Sem linguagem técnica
- Amigável, mas com alertas claros

### 🗣️ Exemplos de respostas:

- "⚠️ Você passou do limite! Bora segurar os gastos."
- "👀 Atenção! Você já está perto do limite."
- "✅ Tudo sob controle, continue assim!"

---

## 🚫 Limitações do Agente

- Não acessa contas bancárias reais
- Não realiza investimentos
- Não substitui um consultor financeiro
- Não toma decisões pelo usuário
- Trabalha apenas com dados informados manualmente

---

## 📚 Etapa 2 - Base de Conhecimento

O agente utiliza regras simples baseadas na comparação entre gasto e limite mensal.

### 📌 Regras do Agente

- Se o gasto for maior que o limite:
  → Emitir alerta de excesso de gastos

- Se o gasto for maior ou igual a 80% do limite:
  → Avisar que está próximo do limite

- Se o gasto for menor que 80% do limite:
  → Informar que está sob controle

---

## 💬 Etapa 3 - Prompts do Agente

### Prompt base utilizado:

O agente foi projetado para responder de forma:

- Curta
- Clara
- Direta
- Sem termos técnicos

### Comportamento esperado:

- Gerar alertas financeiros
- Orientar o usuário de forma simples
- Evitar respostas longas

---

## ⚙️ Etapa 4 - Aplicação Funcional

### 🔁 Arquitetura do Sistema

Usuário informa limite e gasto
↓
Sistema processa os dados
↓
Agente compara valores
↓
Agente retorna resposta


---

## 💻 Código do Projeto

```python
import pandas as pd

def analisar_gasto(gasto_total, limite_mensal):
    percentual = (gasto_total / limite_mensal) * 100

    if gasto_total > limite_mensal:
        return "⚠️ Você passou do limite! Bora segurar os gastos esse mês."
    
    elif percentual >= 80:
        return "👀 Atenção! Você já está perto do limite mensal."
    
    else:
        return "✅ Tudo sob controle. Continue assim!"

def main():
    print("=== GranaCheck ===")
    print("Seu agente simples de controle de gastos\n")

    limite = float(input("Informe seu limite mensal: R$ "))
    gasto = float(input("Informe quanto você já gastou: R$ "))

    resposta = analisar_gasto(gasto, limite)

    dados = {
        "Limite Mensal": [limite],
        "Gasto Atual": [gasto],
        "Saldo Restante": [limite - gasto],
        "Status": [resposta]
    }

    df = pd.DataFrame(dados)

    print("\nResumo financeiro:")
    print(df)

    print("\nResposta do agente:")
    print(resposta)

if __name__ == "__main__":
   main()


```

## 📊 Etapa 5 - Avaliação e Métricas

O agente pode ser avaliado com base em:

- Clareza das respostas
- Correção dos alertas
- Facilidade de uso
- Objetividade na comunicação


## 🧪 Testes Realizados

### ✔️ Cenário 1:
- Limite: 2000
- Gasto: 2500  
→ Resultado: Alerta de excesso

### ✔️ Cenário 2:
- Limite: 2000
- Gasto: 1700  
→ Resultado: Aviso de proximidade

### ✔️ Cenário 3:
- Limite: 2000
- Gasto: 1000  
→ Resultado: Situação controlada


## 🚀 Etapa 6 - Pitch do Projeto

O GranaCheck é um agente financeiro simples e direto, desenvolvido para ajudar usuários a controlar seus gastos mensais.

Através da análise de valores informados, o agente gera alertas inteligentes que auxiliam na tomada de decisão, promovendo maior controle financeiro de forma acessível e prática.


## 👨‍💻 Autor

Renato Oliveira de Jesus
