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
