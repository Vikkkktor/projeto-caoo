from elo1 import Elo1
from elo2 import Elo2
from elo3 import Elo3
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Model:
    def __init__(self):
        self.controller = None

        self.dadosGrapplers = [
            [23, 3.0, 60, 5.5, 100.0, 20.7], 
            [27, 3.5, 50, 7.8, 142.0, 22.0], 
            [23, 5.1, 52, 10.5, 190.0, 24.6], 
            [39, 4.6, 44, 9.1, 164.0, 28.0], 
            [32, 5.4, 37, 10.7, 193.0, 32.6], 
            [13, 5.2, 20, 7.8, 142.0, 27.7], 
        ]

        self.dadosStrikers = [
           [22, 5.9, 37, 8.1, 146.0, 11.9], 
           [52, 5.6, 42, 10.9, 197.0, 45.8], 
           [25, 5.2, 42, 6.0, 108.0, 11.4], 
           [33, 4.5, 48, 9.1, 165.0, 27.7], 
           [26, 3.4, 45, 6.7, 122.0, 21.9], 
           [38, 4.6, 44, 6.6, 120.0, 22.8],
        ]

        self.dadosGerais = self.dadosGrapplers + self.dadosStrikers 

        self.razoesGerais = self.CalcularRazao(self.dadosGerais)
        self.razoesGrapplers = self.CalcularRazao(self.dadosGrapplers)
        self.razoesStrikers = self.CalcularRazao(self.dadosStrikers)

        self.escala = MinMaxScaler()
        self.escalaGrappler = MinMaxScaler()
        self.escalaStriker = MinMaxScaler()
        
        treinoGeral = self.escala.fit_transform(self.razoesGerais)
        self.kmeansGeral = KMeans(n_clusters=2, random_state=42, n_init=10)
        self.kmeansGeral.fit(treinoGeral)
        

        self.idGrappler = self.kmeansGeral.predict([treinoGeral[0]])[0]
        treinoGrappler = self.escalaGrappler.fit_transform(self.razoesGrapplers)
        self.kmeansGrappler = KMeans(n_clusters=2, random_state=42, n_init=10)
        self.kmeansGrappler.fit(treinoGrappler)
        self.idWrestling = self.kmeansGrappler.predict([treinoGrappler[0]])[0]

        treinoStriker = self.escalaStriker.fit_transform(self.razoesStrikers)
        self.kmeansStriker = KMeans(n_clusters=2, random_state=42, n_init=10)
        self.kmeansStriker.fit(treinoStriker)
        self.idBoxe = self.kmeansStriker.predict([treinoStriker[0]])[0]

        self.MostrarGrafico(treinoGeral, self.kmeansGeral, "Macro: Striker vs Grappler")

        self.e0 = Elo1(self)
        self.e1 = Elo2(self)
        self.e2 = Elo3(self)

        self.e0.set_next(self.e1)
        self.e1.set_next(self.e2)


    def set_controller(self, controller):
        self.controller = controller

    def CalcularRazao(self, listaDeTreinamento):
        listaRazoes = []
        for dado in listaDeTreinamento:
            self.forca = dado[1] 
            
            self.mobilidade = dado[2]
            
            self.core = dado[0] 
            
            self.inferior = (dado[4] / 10.0) + dado[5]

            listaRazoes.append([self.forca, self.mobilidade, self.core, self.inferior])

        return listaRazoes


    def MostrarGrafico(self, dadosNorm, modelo, titulo):
        pca = PCA(n_components=2)
        dados2d = pca.fit_transform(dadosNorm)
        centroides2d = pca.transform(modelo.cluster_centers_)
        
        plt.figure(figsize=(8,6))
        plt.scatter(dados2d[:, 0], dados2d[:, 1], c=modelo.labels_, cmap='viridis', s=60, alpha=0.8)
        plt.scatter(centroides2d[:, 0], centroides2d[:, 1], c='red', marker='X', s=200, label='Centroides')
        
        plt.title(titulo)
        plt.xlabel('Componente 1')
        plt.ylabel('Componente 2')
        plt.legend()
        plt.grid(True)
        plt.show()


    def ReceberDados(self, dados):
        resultado = self.e0.run(dados)
        return resultado



