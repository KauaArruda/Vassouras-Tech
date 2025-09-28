# Recomenda Fácil - Vassouras Tech

Algoritmo de recomendação baseado em histórico de compras.
O RecomendaFácil é um algoritmo simples que gera recomendações para clientes com base no tamanho do histórico de compras. Além disso, realiza uma análise de limite e da complexidade assintótica, oferecendo insights sobre a escalabilidade do sistema.

## 🔹 Funcionalidades

1 - Gerar recomendações:

• Calcula o número de recomendações usando a fórmula:

f(n)=2n−1

onde n é o número de itens no histórico de compras.

2 - Simulação de uso:

• Permite simular o comportamento do algoritmo com um histórico de compras fictício.

3 - Análise de limite:

• Calcula o limite da função f(n) para um valor específico de n, demonstrando quantas recomendações seriam geradas nesse ponto.

4 - Análise de complexidade assintótica:

• Mostra o termo dominante da função e explica que a complexidade do algoritmo é O(n) (linear), garantindo alta escalabilidade.

5 - Visualização gráfica:

• Plota o número de recomendações em função do tamanho do histórico, destacando o limite escolhido.

## 🔹 Tecnologias Utilizadas

• Python 3.x

• Bibliotecas:

- matplotlib → Para visualização gráfica.

- numpy → Para manipulação de arrays e geração de sequências numéricas.

## 🔹 Como Usar

1 - Instalar dependências

pip install matplotlib numpy

2- Rodar o código

python recomenda_facil.py

## 🔹 Saída Esperada

--- Simulação de Uso ---
Histórico de Compras (n): 5 itens
Número de Recomendações Geradas: 9
------------------------------
--- Análise de Limite ---
1. Calculando o Limite quando n tende a 10:
   lim (n->10) (2n - 1) = 19
   O limite representa que com 10 compras, 19 recomendações são geradas.
------------------------------
--- Análise da Complexidade Assintótica ---
Função da Complexidade: f(n) = 2n - 1
Termo dominante: 2n
Complexidade Assintótica (Big O): O(n)
Significado: O tempo de execução cresce de forma LINEAR e previsível em relação ao histórico de compras.

## 🔹 Gráfico Gerado

<img width="802" height="574" alt="image" src="https://github.com/user-attachments/assets/d2938081-6111-4436-8c11-adb1afe98c77" />
