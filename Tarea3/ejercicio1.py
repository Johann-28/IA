import time
inicio = time.time()

class Mochila:
    def __init__(self, valor,peso,capacidad):
        self.valor = valor
        self.peso = peso
        self.capacidad = capacidad
        self.f = [] #Valores heurísticos
        self.objetos = []
        self.beneficio = 0

    '''def __init__(self):
        self.valor = []
        self.peso = []
        self.valor = 0'''
    
    def calcularF(self):
        valores = []
        for i in range (0,len(self.valor)):
            valores.append(self.peso[i] + float(self.valor[i]/self.peso[i]))
        
        return valores

    def escogerMinimimo(self):
        self.f = self.calcularF()
        min = self.f[0]
        index = 0
        
        for i in range (0,len(self.f)):
            if self.f[i] <= min:
                min = self.f[i]
                index = i
        
        
        '''print(min)
        print(self.f)'''
        
        self.capacidad -= self.peso[index]

        if self.capacidad < 0:
            return
            
        self.objetos.append(self.valor[index])
        self.f.pop(index)
        self.beneficio += self.valor[index]
        self.valor.pop(index)
        self.peso.pop(index)

        '''print(self.peso)
        print(self.valor)
        print(self.objetos)'''

    def aEstrella(self):
        while self.capacidad >= 0:
            self.escogerMinimimo()



beneficios = [488, 812, 861, 770, 48, 120, 589, 637, 832, 444, 616, 435, 148, 188, 803, 565, 56, 956, 968, 516]
pesos = [575, 62, 516, 369, 922, 491, 575, 897, 450, 488, 610, 430, 212, 271, 353, 830, 46, 414, 176, 801]
capacidad = 6160
x = Mochila(beneficios,pesos,capacidad)
x.aEstrella()
print(x.objetos)
print(x.beneficio)

fin = time.time()

print('Tiempo de ejecucion: ', fin-inicio)