# Função que soma dois arquivos

valor_1 = 3
valor_2 = 5

def soma(valor_1: float, valor_2: float) -> float:
    resultado_da_soma = valor_1 + valor_2
    return resultado_da_soma

valor_3 = soma(valor_1, valor_2)

print(f"o resultado da soma é: {valor_3}")


