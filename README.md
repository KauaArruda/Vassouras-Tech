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

<img width="682" height="258" alt="image" src="https://github.com/user-attachments/assets/46a51ce5-247b-4a82-9746-ee9ca2cde7d8" />

## 🔹 Gráfico Gerado

<img width="802" height="574" alt="image" src="https://github.com/user-attachments/assets/d2938081-6111-4436-8c11-adb1afe98c77" />
