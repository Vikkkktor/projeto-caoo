from elo1 import Elo1
from elo2 import Elo2
from elo3 import Elo3
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Model:
    def __init__(self):
        self.controller = None

        self.listaDeTreinamento = [
            [75, 9.5, 30, 11.0, 5000.0],  # DC
            [80, 10.0, 25, 10.5, 4800.0], # Brock Lesnar
            [70, 9.0, 28, 11.5, 4900.0],  # Randy Couture
            [72, 9.2, 32, 11.0, 5100.0],  # Sonnen

            [60, 8.0, 55, 12.0, 4000.0],  # Demian Maia
            [58, 7.5, 60, 13.0, 4200.0],  # Charles
            [62, 8.2, 50, 12.5, 3800.0],  # Royce Gracie
            [65, 8.5, 52, 12.0, 4100.0],  # Durinho

            [45, 6.5, 35, 17.0, 8000.0],  # Cigano
            [42, 6.0, 30, 18.0, 7500.0],  # Holloway 
            [48, 7.0, 32, 16.5, 7800.0],  # Strickland
            [50, 6.8, 38, 17.5, 7600.0],  # McGregor

            [40, 5.0, 65, 19.0, 9500.0],  # Edson Barboza
            [35, 4.5, 70, 20.0, 10000.0], # Wonderboy
            [45, 5.5, 62, 18.0, 9000.0],  # Adesanya
            [38, 4.8, 60, 18.5, 9200.0],  # Lyoto

            #Dados alunos misturados
            [23, 5.1, 52, 7.0, 4674], 
            [25, 4.2, 40, 5.0, 1751.3],
            [38, 4.6, 44, 4.0, 2736], 
            [33, 5.4, 41, 8.3, 4819.5],
            [27, 3.5, 50, 2.4, 3124], 
            [13, 5.2, 20, 1.7, 3933.4],
            [23, 3, 60, 2.3, 2070], 
            [34, 4.6, 40, 6.3, 1936]
        ]

        self.listaRazao = self.CalcularRazao(self.listaDeTreinamento)

        self.escala = MinMaxScaler()
        
        self.treino = self.escala.fit_transform(self.listaRazao)
        
        self.kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        
        self.kmeans.fit(self.treino)

        self.wrestler = self.kmeans.predict(self.escala.transform([self.listaRazao[0]]))[0]
        self.bjj = self.kmeans.predict(self.escala.transform([self.listaRazao[4]]))[0] 
        self.boxer = self.kmeans.predict(self.escala.transform([self.listaRazao[8]]))[0] 
        self.kicker = self.kmeans.predict(self.escala.transform([self.listaRazao[12]]))[0]

        self.mapaDeEstilos = {
            self.wrestler: "Wrestling",
            self.bjj: "Jiu-Jitsu",
            self.boxer: "Boxe",
            self.kicker: "Muay Thai/Karate"
        }

        self.e0 = Elo1(self)
        self.e1 = Elo2(self, self.kmeans, self.escala, self.mapaDeEstilos)
        self.e2 = Elo3(self)

        self.e0.set_next(self.e1)
        self.e1.set_next(self.e2)


    def set_controller(self, controller):
        self.controller = controller

    def CalcularRazao(self, listaDeTreinamento):
        listaRazoes = []
        for dado in listaDeTreinamento:
            razaoForcaVel = dado[1] / dado[3]
            razaoCoreFlex = dado[0] / dado[2]
            explosao = dado[4]
            flexibilidade = dado[2]

            listaRazoes.append([razaoForcaVel, razaoCoreFlex, explosao, flexibilidade])

        return listaRazoes


    def ReceberDados(self, dados):
        resultado = self.e0.run(dados)
        return resultado



