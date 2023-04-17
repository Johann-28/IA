import time
inicio = time.time()

class Mochila:
    def __init__(self, valor,peso,capacidad):
        self.valor = valor
        self.peso = peso
        self.capacidad = capacidad
        self.f = [] #Valores heurísticos
        self.objetos = []
        self.valores = []
        self.pesos = []
        self.beneficio = 0

    
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
        
        
        self.capacidad -= self.peso[index]

        if self.capacidad < 0:
            return
            
        self.objetos.append(index)
        self.valores.append(self.valor[index])
        self.pesos.append(self.peso[index])
        
        self.f.pop(index)
        self.beneficio += self.valor[index]
        self.valor.pop(index)
        self.peso.pop(index)

       

    def aEstrella(self):
        while self.capacidad >= 0:
            self.escogerMinimimo()




pesos =  [32, 52, 15, 23, 67, 23, 84, 96, 76, 4, 40, 53, 21, 10, 35, 23, 64, 71, 59, 99, 53, 48, 24, 89, 39, 6, 45, 80, 62, 60, 49, 74, 35, 89, 5, 36, 50, 61, 89, 8, 72, 77, 47, 9, 37, 47, 67, 46, 7, 98, 35, 13, 37, 22, 52, 29, 84, 23, 27, 27, 46, 77, 3, 28, 13, 92, 34, 51, 18, 72, 40, 31, 37, 85, 78, 6, 68, 23, 32, 7, 46, 28, 56, 8, 71, 92, 61, 18, 15, 62, 9, 33, 90, 84, 29, 84, 12, 23, 89, 58, 69, 64, 47, 25]
beneficios =  [10, 24, 15, 35, 7, 11, 78, 88, 34, 87, 30, 58, 13, 30, 61, 78, 45, 9, 2, 12, 87, 58, 90, 8, 91, 89, 73, 75, 20, 68, 60, 46, 30, 59, 56, 29, 10, 35, 52, 6, 6, 28, 69, 14, 97, 17, 48, 33, 83, 56, 62, 27, 29, 49, 7, 95, 64, 64, 4, 58, 18, 17, 92, 50, 28, 13, 56, 35, 36, 81, 25, 17, 31, 48, 30, 29, 73, 58, 24, 48, 34, 17, 67, 16, 2, 67, 47, 61, 97, 95, 77, 17, 5, 51, 47, 48, 73, 85, 72, 48, 30, 6, 13, 23]


capacidad =  500
x = Mochila(beneficios,pesos,capacidad)
x.aEstrella()
print('objetos: ', x.objetos)
print('beneficios: ', x.beneficio)
print('peso: ', x.pesos )
print('valores: ',x.valores)
print('capacidad: ' , capacidad)

fin = time.time()

print('Tiempo de ejecucion: ', fin-inicio)