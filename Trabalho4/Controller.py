from Busca import Busca
import random
class Controller:
    def __init__(self):
        self.busca = Busca()
        self.map = [[100 for i in range(34)] for j in range(59)]
        self.map2 = [[False for i in range(34)] for j in range(59)]
        self.ESTADO_ATUAL = "Explorar"
        self.action = None
        self.destino = [random.randint(0, 20),random.randint(15, 33)]
        self.observation = False
        self.hits = 0
    
    def explorar(self):
        self.busca.mapa = self.map
        self.busca.busca_heuristica([self.position.x,self.position.y], self.destino)
        path = self.busca.caminho
        if len(path) < 3:
            self.destino = [random.randint(0, 20),random.randint(15, 33)]
            return
        
        next_position = path[-2]
        self.proximo_movimento(next_position)
    
    def proximo_movimento(self, next_position):
        if self.position.x - next_position[0] == 0:
            if self.dir == "north":
                self.action = "andar" if self.position.y > next_position[1] else "virar_esquerda"
            elif self.dir == "south":
                self.action = "andar" if self.position.y < next_position[1] else "virar_esquerda"
            elif self.dir == "east":
                self.action = "virar_direita" if self.position.y < next_position[1] else "virar_esquerda"
            elif self.dir == "west":
                self.action = "virar_direita" if self.position.y > next_position[1] else "virar_esquerda"
        
        elif self.position.y - next_position[1] == 0:
            if self.dir == "north":
                self.action = "virar_direita" if self.position.x < next_position[0] else "virar_esquerda"
            elif self.dir == "south":
                self.action = "virar_direita" if self.position.x > next_position[0] else "virar_esquerda"
            elif self.dir == "east":
                self.action = "virar_esquerda" if self.position.x > next_position[0] else "andar"
            elif self.dir == "west":
                self.action = "virar_esquerda" if self.position.x < next_position[0] else "andar"

    def atualizarFrente(self):
        self.map[self.position.x][self.position.y] = 1
        self.map2[self.position.x][self.position.y] = True
        if self.dir == "north":
            self.map[self.position.x][self.position.y-1] = 10000
            self.map2[self.position.x][self.position.y-1] = True
        elif self.dir == "south":
            self.map[self.position.x][self.position.y+1] = 10000
            self.map2[self.position.x][self.position.y+1] = True
        elif self.dir == "east":
            self.map[self.position.x+1][self.position.y] = 10000
            self.map2[self.position.x+1][self.position.y] = True
        elif self.dir == "west":
            self.map[self.position.x-1][self.position.y] = 10000
            self.map2[self.position.x-1][self.position.y] = True

    def atualizarAdjancentes(self, value):
        if not self.map2[self.position.x][self.position.y]:
            self.map[self.position.x][self.position.y] = 1
            self.map2[self.position.x][self.position.y] = True
            if self.dir == "north":
                self.atualizarposition(self.position.y-1,False,value)
            elif self.dir == "south":
                self.atualizarposition(self.position.y+1,False,value)
            elif self.dir == "east":
                self.atualizarposition(self.position.x+1,True,value)
            elif self.dir == "west":
                self.atualizarposition(self.position.x-1,True,value)

    def atualizarposition(self, position, iscordx, value):
        if iscordx:
            if (position <= 58  and position >= 0):
                if not self.map2[position][self.position.y]:
                    self.map[position][self.position.y] = value[0]
                    self.map2[position][self.position.y] = value[1]
                if self.position.y > 0 and not self.map2[self.position.x][self.position.y-1]:
                    self.map[self.position.x][self.position.y-1] = value[0]
                    self.map2[self.position.x][self.position.y-1] = value[1]
                if self.position.y < 33 and not self.map2[self.position.x][self.position.y+1]:
                    self.map[self.position.x][self.position.y+1] = value[0]
                    self.map2[self.position.x][self.position.y+1] = value[1]
        else:
            if (position <= 33  and position >= 0):
                if not self.map2[self.position.x][position]:
                    self.map[self.position.x][position] = value[0]
                    self.map2[self.position.x][position] = value[1]
                if self.position.x < 58 and not self.map2[self.position.x+1][self.position.y]:
                    self.map[self.position.x+1][self.position.y] = value[0]
                    self.map2[self.position.x+1][self.position.y] = value[1]
                if self.position.x > 0 and not self.map2[self.position.x-1][self.position.y]:
                    self.map[self.position.x-1][self.position.y] = value[0]
                    self.map2[self.position.x-1][self.position.y] = value[1]