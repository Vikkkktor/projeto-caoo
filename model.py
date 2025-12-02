from elo1 import Elo1
from elo2 import Elo2
from elo3 import Elo3
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pymongo
import json

class Model:
    def __init__(self):
        self.controller = None

        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client["usuariosBD"]
        self.collection = self.db["dadosTreinamento"]
        with open("dadosDB.json", "r") as arquivo:
            arquivoJson = json.load(arquivo)
        self.collection.insert_one(arquivoJson)

        self.TreinarAlgoritmos()

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


    def TreinarAlgoritmos(self):
        self.dataset = self.collection.find_one({"tipo_dataset": "treinamento-inicial"})

        self.dadosGrapplers = self.dataset["dadosGrapplers"]

        self.dadosStrikers = self.dataset["dadosStrikers"]

        self.dadosGerais = self.dadosGrapplers + self.dadosStrikers 

        self.razoesGerais = self.CalcularRazao(self.dadosGerais)
        self.razoesGrapplers = self.CalcularRazao(self.dadosGrapplers)
        self.razoesStrikers = self.CalcularRazao(self.dadosStrikers)

        self.escala = MinMaxScaler()
        self.escalaGrappler = MinMaxScaler()
        self.escalaStriker = MinMaxScaler()
        
        self.treinoGeral = self.escala.fit_transform(self.razoesGerais)
        self.kmeansGeral = KMeans(n_clusters=2, random_state=42, n_init=10)
        self.kmeansGeral.fit(self.treinoGeral)

        self.idGrappler = self.kmeansGeral.predict([self.treinoGeral[0]])[0]
        self.treinoGrappler = self.escalaGrappler.fit_transform(self.razoesGrapplers)
        self.kmeansGrappler = KMeans(n_clusters=2, random_state=42, n_init=10)
        self.kmeansGrappler.fit(self.treinoGrappler)
        self.idWrestling = self.kmeansGrappler.predict([self.treinoGrappler[0]])[0]

        self.treinoStriker = self.escalaStriker.fit_transform(self.razoesStrikers)
        self.kmeansStriker = KMeans(n_clusters=2, random_state=42, n_init=10)
        self.kmeansStriker.fit(self.treinoStriker)
        self.idBoxe = self.kmeansStriker.predict([self.treinoStriker[0]])[0]


    def MostrarGrafico(self, dadosNorm, modelo, titulo, pontoUsuario=None):
        pca = PCA(n_components=2)
        dados2d = pca.fit_transform(dadosNorm)
        centroides2d = pca.transform(modelo.cluster_centers_)
        
        plt.figure(figsize=(8,6))

        indiceGrapplers = np.where(modelo.labels_ == self.idGrappler)
        indicesStrikers = np.where(modelo.labels_ != self.idGrappler)

        plt.scatter(dados2d[indiceGrapplers, 0], dados2d[indiceGrapplers, 1], c='purple', s=70, alpha=0.8, label='Grapplers')
        plt.scatter(dados2d[indicesStrikers, 0], dados2d[indicesStrikers, 1], c='orange', s=70, alpha=0.8, label='Strikers')
        plt.scatter(centroides2d[:, 0], centroides2d[:, 1], c='red', marker='X', s=200, label='Centroides')

        if pontoUsuario is not None:
            usuario2d = pca.transform(pontoUsuario)
            plt.scatter(usuario2d[:, 0], usuario2d[:, 1], c='#ff00ff', marker='*', s=200, label='VOCÊ', edgecolors='black')

        plt.title(titulo)
        plt.xlabel('Estilo: Controle (Grappling) vs Explosão (Striking)')
        plt.ylabel('Performance Atlética')
        plt.legend()
        plt.grid(True)
        plt.show()


    def ReceberDados(self, dados):
        resultado = self.e0.run(dados)
        return resultado



