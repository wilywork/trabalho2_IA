'''
#BUSCA EM LARGURA UTILIZANDO HEURISTICA DE MINIMOS CONFLITOS
Essa heurística ajuda a minimizar o número de conflitos
durante o preenchimento das colunas e aumentama chance de encontrar 
soluções com menos retrocessos.
'''

import time

inicio = time.time()

# defini a função de busca em largura
def bfsRainhas(tamanhoTabuleiro):
    solucoes = []
    contadorPassos = [0]

    # defini a estrutura inicial
    fila = [([None] * tamanhoTabuleiro, 0)]  #(tabuleiro, colunaAtual)

    while fila:
        tabuleiro, colunaAtual = fila.pop(0)
        contadorPassos[0] += 1

        # se todas as colunas estão preenchidas = armazena a solução
        if colunaAtual == tamanhoTabuleiro:
            solucoes.append(tabuleiro[:])
            continue

        # ordena as linhas pela coluna com menos chance de ataques
        linhasOrdenadas = ordenarLinhasMenosAtaques(tabuleiro, colunaAtual)

        for linha in linhasOrdenadas:
            if posicaoSegura(tabuleiro, colunaAtual, linha):
                novoTabuleiro = tabuleiro[:]
                novoTabuleiro[colunaAtual] = linha
                fila.append((novoTabuleiro, colunaAtual + 1))

    return [solucoes, contadorPassos[0]]

# heurística: coluna com menos chance de ataque
def ordenarLinhasMenosAtaques(tabuleiro, coluna):
    ataquesPotenciais = []
    for linha in range(len(tabuleiro)):
        # calcula os ataques para cada linha
        ataques = calcularAtaquesPotenciais(tabuleiro, coluna, linha)
        ataquesPotenciais.append((linha, ataques))
    # ordena as linhas de acordo com o número de ataques
    ataquesPotenciais.sort(key=lambda x: x[1])
    return [linha for linha, _ in ataquesPotenciais]

# calcula o número de ataques em uma linha
def calcularAtaquesPotenciais(tabuleiro, colunaAtual, linhaAtual):
    ataques = 0
    tamanhoTabuleiro = len(tabuleiro)
    for colunaFutura in range(colunaAtual + 1, tamanhoTabuleiro):
        for linhaFutura in range(tamanhoTabuleiro):
            if not posicaoSegura(tabuleiro, colunaFutura, linhaFutura):
                ataques += 1
    return ataques

# verifica se a posição é segura
def posicaoSegura(tabuleiro, coluna, linha):
    for i in range(coluna):
        if tabuleiro[i] is None:
            continue
        if tabuleiro[i] == linha or abs(tabuleiro[i] - linha) == abs(i - coluna):
            return False
    return True


# inicio
# define o tamanho do tabuleiro
tamanhoTabuleiro = 8
# chama a função para iniciar a solucao
solucoes, contadorPassos = bfsRainhas(tamanhoTabuleiro)

# exibir o total de passos
print(f"Total de passos: {contadorPassos}")

# caso não encontrar nenhuma solução retorna um erro
if len(solucoes) == 0:
    raise Exception("Nenhuma solução encontrada.")

# exibi todas as soluções encontradas
for idx, solucao in enumerate(solucoes, 1):
    print(f"Solução {idx}:")
    for i in range(len(solucao)):
        linha = []
        for j in range(len(solucao)):
            if solucao[j] == i:
                linha.append("R")
            else:
                linha.append(".")
        print(" ".join(linha))
    print()


fim = time.time()
print(f'Tempo total: {fim - inicio:.2f} segundos')
