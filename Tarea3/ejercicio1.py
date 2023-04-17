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
            
        self.objetos.append(self.valor[index])
        self.f.pop(index)
        self.beneficio += self.valor[index]
        self.valor.pop(index)
        self.peso.pop(index)

       

    def aEstrella(self):
        while self.capacidad >= 0:
            self.escogerMinimimo()



pesos = [100, 94, 506, 416, 992, 649, 237, 457, 815, 446, 422, 791, 359, 667, 598, 7, 544, 334, 766, 994, 893, 633, 131, 428, 700, 617, 874, 720, 419, 794, 196, 997, 116, 908, 539, 707, 569, 537, 931, 726, 487, 772, 513, 81, 943, 58, 303, 764, 536, 724, 789, 479, 142, 339, 641, 196, 494, 66, 824, 208, 711, 800, 314, 289, 401, 466, 689, 833, 225, 244, 849, 113, 379, 361, 65, 486, 686, 286, 889, 24, 491, 891, 90, 181, 214, 17, 472, 418, 419, 356, 682, 306, 201, 385, 952, 500, 194, 737, 324, 992, 224]

beneficios = [995, 485, 326, 248, 421, 322, 795, 43, 845, 955, 252, 9, 901, 122, 94, 738, 574, 715, 882, 367, 984, 299, 433, 682, 72, 874, 138, 856, 145, 995, 529, 199, 277, 97, 719, 242, 107, 122, 70, 98, 600, 645, 267, 972, 895, 213, 748, 487, 923, 29, 674, 540, 554, 467, 46, 710, 553, 191, 724, 730, 988, 90, 340, 549, 196, 865, 678, 570, 936, 722, 651, 123, 431, 508, 585, 853, 642, 992, 725, 286, 812, 859, 663, 88, 179, 187, 619, 261, 846, 192, 261, 514, 886, 530, 849, 294, 799, 391, 330, 298, 790]

capacidad =  10000
x = Mochila(beneficios,pesos,capacidad)
x.aEstrella()
print(x.objetos)
print(x.beneficio)

fin = time.time()

print('Tiempo de ejecucion: ', fin-inicio)