from elo import Elo

class Elo2(Elo):
    def __init__(self, model, kmeans, escala, mapaDeEstilos):
      self.kmeans = kmeans
      self.escala = escala
      self.mapa = mapaDeEstilos
      super().__init__(model)

    def processamento(self, dados):
        self.razaoForcaVel = dados[1] / dados[3]
        self.razaoCoreFlex = dados[0] / dados[2]
        self.explosao = dados[4]
        self.flexibilidade = dados[2]

        self.dadosUsuario = [[self.razaoForcaVel, self.razaoCoreFlex, self.explosao, self.flexibilidade]]
        self.dadosUsuarioNormalizado = self.escala.transform(self.dadosUsuario)
        self.clusterId = self.kmeans.predict(self.dadosUsuarioNormalizado)[0]

        arteMarcialSugerida = self.mapa.get(self.clusterId)
       
        return arteMarcialSugerida