import numpy as np


# Criar um array bidimensional com dados diferentes dos utilizados em sala

matriz = np.array([[10, 6, 4, 0], [3, 4, 8, 13], [5, 8, 3, 2]])
# np.savetxt('array.txt', matriz, delimiter=',')

m1 = np.genfromtxt('array.txt', delimiter=",", dtype="float64")
print(m1, '\n')


# Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis)

max_linhas = m1.max(axis = 1) # valor máximo de cada linha
print(max_linhas, '\n')

mean_por_coluna = m1.mean(axis = 0) # valor médio por coluna
print(mean_por_coluna, '\n')

min_do_array = m1.min() # menor valor de todo o array
print(min_do_array, '\n')

# Obter a transposta da matriz e realizar uma operação com ela

m2 = m1_transposta = m1.T
print(m1_transposta, '\n')
m2_mais_50pct = m2 * 1.5
print(m2_mais_50pct, '\n')

# Realizar um produto escalar entre duas matrizes ou de um array com uma matriz

prod_escalar = m2@m1
print(prod_escalar, '\n')

# Criar um filtro para a sua matriz

pares = m1[m1%2 == 0]
print(pares, '\n')

# Realizar alguma operação aritmética (número com matriz, array com matriz, etc.)

dif_acresc = m2_mais_50pct - m2
print(dif_acresc)

# Vincular com o github (código deve estar no repositório sem o venv ou outros arquivos de configuração)
