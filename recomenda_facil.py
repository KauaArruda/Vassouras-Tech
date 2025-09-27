import matplotlib.pyplot as plt
import numpy as np

def gerarRecomendacoes(historico_compras):
    n = len(historico_compras)
    recomendacoes = (2 * n) - 1
    return recomendacoes, n

historico_cliente = ["Vassoura A", "Pano de chão", "Rodo Y", "Balde Z", "Esponja"]
numero_recomendacoes, n_compras = gerarRecomendacoes(historico_cliente)

print("--- Simulação de Uso ---")
print(f"Histórico de Compras (n): {n_compras} itens")
print(f"Número de Recomendações Geradas: {numero_recomendacoes}")
print("-" * 30)

def limite_recomendacoes(n_alvo):
    return (2 * n_alvo) - 1

n_limite = 10
limite_resultado = limite_recomendacoes(n_limite)

print("--- Análise de Limite ---")
print(f"1. Calculando o Limite quando n tende a {n_limite}:")
print(f"   lim (n->10) (2n - 1) = {limite_resultado}")
print(f"   O limite representa que com 10 compras, 19 recomendações são geradas.")
print("-" * 30)

print("--- Análise da Complexidade Assintótica ---")
print("Função da Complexidade: f(n) = 2n - 1")
print("Termo dominante: 2n")
print("Complexidade Assintótica (Big O): O(n)")
print("Significado: O tempo de execução do algoritmo cresce de forma LINEAR e PREVISÍVEL")
print("             em relação ao tamanho do histórico de compras (n), garantindo alta escalabilidade.")

n_valores = np.arange(1, 16) 

f_n_valores = 2 * n_valores - 1

plt.figure(figsize=(8, 5))
plt.plot(n_valores, f_n_valores, marker='o', linestyle='-', color='blue')
plt.plot(10, limite_resultado, 'ro', label=f'Limite n=10 ({10}, {limite_resultado})')
plt.title('Variação de Recomendações: f(n) = 2n - 1')
plt.xlabel('n (Histórico de Compras)')
plt.ylabel('f(n) (Número de Recomendações)')
plt.grid(True, linestyle='--')
plt.legend()
plt.xticks(n_valores)
plt.yticks(f_n_valores)
plt.show()