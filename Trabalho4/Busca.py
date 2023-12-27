import math


class Busca():

    def __init__(self):
        self.mapa = None
        self.caminho = []

    # Faz a busca entre dois campos
    def busca_heuristica(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino
        self.caminho = []
        abertas = []
        expandidas = []
        abertas.append(self.inicio)
        custo_heuristico = [0]  # lista que calcula o custo heuristico mais deslocamento
        self.custo = [0]  # custo do deslocamento
        lista_ant = []
        lista_atual = []

        while (len(abertas) > 0):
            atual = abertas[self.M_custo(custo_heuristico)]
            expandidas.append(atual)

            if atual == self.destino:
                self.desc_caminho(lista_atual, lista_ant, atual)
                return self.M_custo(self.custo)
            else:
                adj = self.add_adjacentes(atual, abertas, expandidas, custo_heuristico)
                del (custo_heuristico[abertas.index(atual)])
                del (self.custo[abertas.index(atual)])
                abertas.remove(atual)
                self.add_ant_lista(lista_ant, lista_atual, atual, adj)

    # Exibe o caminho em caminho.txt
    def exibe_caminho(self):
        mapa = []
        for i in self.mapa:
            mapa.append(i.copy())
        for cord in self.caminho:
            i, j = cord
            mapa[i][j] = '*'

        file = open('caminho.txt', 'w')
        for i in mapa:
            file.writelines(i)
        file.close()

    # Metodos Auxiliares

    def desc_caminho(self, lista_atual, ant, atual):
        atual = self.destino
        self.caminho.append(atual)
        while atual != self.inicio:
            for x in range(len(lista_atual)):
                if atual in lista_atual[x]:
                    ind = x
            atual = ant[ind]
            self.caminho.append(atual)

    def add_ant_lista(self, lista_atual, ant, atual, adj):
        ant.append(adj)
        lista_atual.append(atual)

    # Adiciona os campos adjacentes na lista de abertas e os seus custos na lista de custo
    def add_adjacentes(self, atual, abertas, expandidas, custo):
        i, j = atual
        adj = []
        if j - 1 >= 0 and [i, j - 1] not in abertas and [i, j - 1] not in expandidas:
            abertas.append([i, j - 1])
            custo.append(self.custo_total([i, j - 1], custo[abertas.index([i, j])], abertas.index([i, j])))
            adj.append([i, j - 1])
        if j + 1 < len(self.mapa[i]) - 1 and [i,j + 1] not in abertas and [i, j + 1] not in expandidas:
            abertas.append([i, j + 1])
            custo.append(self.custo_total([i, j + 1], custo[abertas.index([i, j])], abertas.index([i, j])))
            adj.append([i, j + 1])
        if i - 1 >= 0 and [i - 1, j] not in abertas and [i - 1, j] not in expandidas:
            abertas.append([i - 1, j])
            custo.append(self.custo_total([i - 1, j], custo[abertas.index([i, j])], abertas.index([i, j])))
            adj.append([i - 1, j])
        if i + 1 < len(self.mapa) and [i + 1,j] not in abertas and [i + 1, j] not in expandidas:
            abertas.append([i + 1, j])
            custo.append(self.custo_total([i + 1, j], custo[abertas.index([i, j])], abertas.index([i, j])))
            adj.append([i + 1, j])
        return adj

    # Calcula o custo e o custo heuristico
    def custo_total(self, posicao, c_ant, index):
        i, j = posicao
        custo = self.mapa[i][j]

        self.custo.append(custo + self.custo[index])
        custo += c_ant + self.dist_heuristica(posicao) / 3
        return custo

    def dist_heuristica(self, atual):
        x = abs(atual[1] - self.destino[1])
        y = abs(atual[0] - self.destino[0])
        res = math.sqrt(x * x + y * y)

        return res

    def M_custo(self, custo):
        c = custo[0]
        x = 0
        for i in range(len(custo)):
            if c > custo[i]:
                c = custo[i]
                x = i
        return x